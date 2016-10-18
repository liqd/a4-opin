var React = require('react')
var h = require('react-hyperscript')
var django = require('django')

module.exports.CommentEditForm = React.createClass({
  getInitialState: function () {
    return {comment: this.props.comment}
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
      comment: comment
    })
  },
  render: function () {
    return (
      h('form.general-form', { onSubmit: this.handleSubmit }, [
        h('div.form-group', [
          h('textarea.form-control', {
            type: 'text',
            placeholder: django.gettext('Your comment here'),
            rows: this.props.rows,
            value: this.state.comment,
            onChange: this.handleTextChange,
            required: 'required'
          })
        ]),
        h('input.submit-button', {
          type: 'submit',
          value: django.gettext('post')
        }),
        h('input.cancel-button', {
          type: 'submit',
          value: django.gettext('cancel'),
          onClick: this.props.handleCancel
        })
      ])
    )
  }
})

module.exports.CommentEditForm.contextTypes = {
  isAuthenticated: React.PropTypes.boolen,
  login_url: React.PropTypes.string
}
