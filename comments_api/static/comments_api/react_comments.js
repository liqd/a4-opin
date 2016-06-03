/**
 * This file provided by Facebook is for non-commercial testing and evaluation
 * purposes only. Facebook reserves all rights not expressly granted.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * FACEBOOK BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

(function () {
  function getCookie(c_name)
  {
    if (document.cookie.length > 0)
    {
      var c_start = document.cookie.indexOf(c_name + "=");
      if (c_start != -1)
      {
        c_start = c_start + c_name.length + 1;
        var c_end = document.cookie.indexOf(";", c_start);
        if (c_end == -1) c_end = document.cookie.length;
        return unescape(document.cookie.substring(c_start,c_end));
      }
    }
    return "";
  }

  $(function () {
    $.ajaxSetup({
      headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
  });

  var Comment = React.createClass({
    rawMarkup: function() {
      var rawMarkup = marked(this.props.children.toString(), {sanitize: true});
      return { __html: rawMarkup };
    },

    render: function() {
      return (
        h('div.comment', [
          h('h2.commentAuthor', this.props.userName),
          h('span', {
            dangerouslySetInnerHTML: this.rawMarkup()
          })
        ])
      );
    }
  });

  var CommentBox = React.createClass({
    loadCommentsFromServer: function() {
      $.ajax({
        url: this.props.url,
        dataType: 'json',
        cache: false,
        success: function(data) {
          this.setState({data: data});
        }.bind(this),
        error: function(xhr, status, err) {
          console.error(this.props.url, status, err.toString());
        }.bind(this)
      });
    },
    handleCommentSubmit: function(comment) {
      $.ajax({
        url: this.props.url,
        dataType: 'json',
        type: 'POST',
        data: comment,
        success: function(new_comment) {
          var comments = this.state.data;
          var newComments = comments.concat([new_comment]);
          this.setState({data: newComments});
        }.bind(this),
        error: function(xhr, status, err) {
          console.error(this.props.url, status, err.toString());
        }.bind(this)
      });
    },
    getInitialState: function() {
      return {data: []};
    },
    componentDidMount: function() {
      this.loadCommentsFromServer();
      setInterval(this.loadCommentsFromServer, this.props.pollInterval);
    },
    render: function() {
      return (
        h('div.commentBox', [
          h('h1', 'Comments'),
          h(CommentList, { data: this.state.data }),
          h(CommentForm, { subjectType: this.props.subjectType,
                           subjectId: this.props.subjectId,
                           onCommentSubmit: this.handleCommentSubmit
                         }),
        ])
      );
    }
  });

  var CommentList = React.createClass({
    render: function() {
      var commentNodes = this.props.data.map(function(comment) {
        return (
          h(Comment, { userName: comment.user_name }, comment.comment)
        );
      });

      return (
        h('div.commentList', commentNodes)
      );
    }
  });

  var CommentForm = React.createClass({
    getInitialState: function() {
      return {comment: '' };
    },
    handleTextChange: function(e) {
      this.setState({comment: e.target.value});
    },
    handleSubmit: function(e) {
      e.preventDefault();
      var comment = this.state.comment.trim();
      if (!comment) {
        return;
      }
      this.props.onCommentSubmit({
        comment: comment,
        object_pk: this.props.subjectId,
        content_type: this.props.subjectType});
      this.setState({comment: ''});
    },
    render: function() {
      return (
        h('form.commentForm', { onSubmit: this.handleSubmit }, [
          h('input', {
            type: 'text',
            placeholder: 'Say somehting..',
            value: this.state.comment,
            onChange: this.handleTextChange
          }),
          h('input', {
            type: 'submit',
            value: 'Post'
          })
        ])
      );
    }
  });

  window._opin = window._opin || {}

  window._opin.renderComment = function (subjectType, subjectId, target) {
    ReactDOM.render(
      h(CommentBox, {
        url: '/api/comments/',
        subjectType: subjectType,
        subjectId: subjectId,
        pollInterval: 2000
      }),
      document.getElementById(target));
  }
}());
