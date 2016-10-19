var config = require('../../../contrib/static/js/config')

var React = require('react')
var django = require('django')

let CommentForm = React.createClass({
  getInitialState: function () {
    return {comment: ''}
  },
  handleTextChange: function (e) {
    this.setState({comment: e.target.value})
  },
  handleSubmit: function (e) {
    e.preventDefault()
    var comment = this.state.comment.trim()
    if (!comment) {
      return
    }
    this.props.onCommentSubmit({
      comment: comment,
      object_pk: this.props.subjectId,
      content_type: this.props.subjectType
    }, this.props.parentIndex)
    this.setState({comment: ''})
  },
  render: function () {
    if (this.context.isAuthenticated) {
      return (
        <form className="general-form" onSubmit={this.handleSubmit}>
          <div className="form-group">
            <textarea rows={this.props.rows} className="form-control"
              placeholder={django.gettext('Your comment here')}
              onChange={this.handleTextChange} required="required" defaultValue={this.state.comment} />
          </div>
          <input type="submit" value={django.gettext('post')} className="submit-button" />
        </form>
      )
    } else {
      return (
        <div className="comments_login">
          <a href={config.loginUrl}>{django.gettext('Please login to comment')}</a>
        </div>
      )
    }
  }
})

CommentForm.contextTypes = {
  isAuthenticated: React.PropTypes.bool
}

module.exports = CommentForm

