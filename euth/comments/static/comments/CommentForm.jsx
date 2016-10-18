var React = require('react')
var h = require('react-hyperscript')
var django = require('django')

module.exports.CommentForm = React.createClass({
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
        h('form.general-form', { onSubmit: this.handleSubmit }, [
          h('div.form-group', [
            h('textarea.form-control', {
              type: 'text',
              placeholder: this.props.placeholder,
              rows: this.props.rows,
              value: this.state.comment,
              onChange: this.handleTextChange,
              required: 'required'
            })
          ]),
          h('input.submit-button', {
            type: 'submit',
            value: django.gettext('post')
          })
        ])
      )
    } else {
      return (
        h('div.comments_login', [
          h('a', {href: this.context.login_url}, django.gettext('Please login to comment'))
        ])
      )
    }
  }
})

module.exports.CommentForm.contextTypes = {
  isAuthenticated: React.PropTypes.bool,
  login_url: React.PropTypes.string
}
