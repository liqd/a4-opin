var CommentList = require('./CommentList')
var CommentForm = require('./CommentForm')
var api = require('../../../contrib/static/js/api')

var React = require('react')
var update = require('react-addons-update')
var moment = require('moment')
var django = require('django')

module.exports.CommentBox = React.createClass({
  loadCommentsFromServer: function () {
    api.comments.get({
      object_pk: this.props.subjectId,
      content_type: this.props.subjectType
    }).done(function (comments) {
      this.setState({
        comments: comments
      })
    }.bind(this))
  },
  updateStateComment: function (index, parentIndex, updatedComment) {
    var comments = this.state.comments
    var diff = {}
    if (typeof parentIndex !== 'undefined') {
      diff[parentIndex] = { child_comments: {} }
      diff[parentIndex].child_comments[index] = { $merge: updatedComment }
    } else {
      diff[index] = { $merge: updatedComment }
    }
    comments = update(comments, diff)
    this.setState({ comments: comments })
  },
  handleCommentSubmit: function (comment, parentIndex) {
    api.comments.add(comment)
      .done(function (comment) {
        var comments = this.state.comments
        var diff = {}
        if (typeof parentIndex !== 'undefined') {
          diff[parentIndex] = { child_comments: { $push: [ comment ] } }
        } else {
          diff = { $unshift: [ comment ] }
        }
        this.setState({
          comments: update(comments, diff)
        })
      }.bind(this))
  },
  handleCommentModify: function (commentText, index, parentIndex) {
    var comments = this.state.comments
    var comment = comments[index]
    if (typeof parentIndex !== 'undefined') {
      comment = comments[parentIndex].child_comments[index]
    }

    api.comments.change({
      comment: commentText, id: comment.id
    }, comment.id)
      .done(this.updateStateComment.bind(this, index, parentIndex))
  },
  handleCommentDelete: function (index, parentIndex) {
    var comments = this.state.comments
    var comment = comments[index]
    if (typeof parentIndex !== 'undefined') {
      comment = comments[parentIndex].child_comments[index]
    }

    api.comments.delete(comment.id)
      .done(this.updateStateComment.bind(this, index, parentIndex))
  },
  getInitialState: function () {
    return {
      comments: []
    }
  },
  componentDidMount: function () {
    this.loadCommentsFromServer()
    setInterval(this.loadCommentsFromServer, this.props.pollInterval)
    moment.locale(this.props.language)
  },
  getChildContext: function () {
    return {
      isAuthenticated: this.props.isAuthenticated,
      isModerator: this.props.isModerator,
      login_url: this.props.login_url,
      ratingsUrls: this.props.ratingsUrls,
      comments_contenttype: this.props.comments_contenttype,
      user_name: this.props.user_name,
      language: this.props.language
    }
  },
  render: function () {
    if (this.props.isReadOnly) {
      var commentBox = (
        <div className="commentBox">
          <CommentForm subjectType={this.props.subjectType} subjectId={this.props.subjectId}
            onCommentSubmit={this.handleCommentSubmit} placeholder={django.getText('Your comment here')}
            rows="5" />
        </div>
      )
    }
    return (
      <div>
        <div className="black-divider">{this.state.comments.length + ' ' + django.ngettext('comment', 'comments', this.state.comments.length)}</div>
        {commentBox}
        <div className="comment-list">
          <CommentList comments={this.state.comments} handleCommentDelete={this.handleCommentDelete}
            handleCommentSubmit={this.handleCommentSubmit} handleCommentModify={this.handleCommentModify}
            isReadOnly={this.props.isReadOnly} />
        </div>
      </div>
    )
  }
})

module.exports.CommentBox.childContextTypes = {
  isAuthenticated: React.PropTypes.bool,
  isModerator: React.PropTypes.bool,
  login_url: React.PropTypes.string,
  ratingsUrls: React.PropTypes.string,
  comments_contenttype: React.PropTypes.number,
  user_name: React.PropTypes.string,
  language: React.PropTypes.string
}
