var $ = require('jquery')
var React = require('react')
var ReactDOM = require('react-dom')
var h = require('react-hyperscript')
var update = require('react-addons-update')
var marked = require('marked')
var moment = require('moment')
var cookie = require('js-cookie')
var django = require('django')

$(function () {
  $.ajaxSetup({
    headers: { 'X-CSRFToken': cookie.get('csrftoken') }
  })
})

var CommentBox = React.createClass({
  loadCommentsFromServer: function () {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      data: {
        object_pk: this.props.subjectId,
        content_type: this.props.subjectType
      },
      success: function (comments) {
        this.setState({
          comments: comments
        })
      }.bind(this),
      error: function (xhr, status, err) {
        console.error(this.props.url, status, err.toString())
      }.bind(this)
    })
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
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: comment,
      success: function (comment) {
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
      }.bind(this),
      error: function (xhr, status, err) {
        console.error(this.props.url, status, err.toString())
      }.bind(this)
    })
  },
  handleCommentModify: function (commentText, index, parentIndex) {
    var comments = this.state.comments
    var comment = comments[index]
    if (typeof parentIndex !== 'undefined') {
      comment = comments[parentIndex].child_comments[index]
    }

    $.ajax({
      url: this.props.url + comment.id + '/',
      dataType: 'json',
      type: 'PATCH',
      data: { comment: commentText, id: comment.id },
      success: this.updateStateComment.bind(this, index, parentIndex),
      error: function (xhr, status, err) {
        console.error(this.props.url + comment.id + '/', status, err.toString())
      }.bind(this)
    })
  },
  handleCommentDelete: function (index, parentIndex) {
    var comments = this.state.comments
    var comment = comments[index]
    if (typeof parentIndex !== 'undefined') {
      comment = comments[parentIndex].child_comments[index]
    }

    $.ajax({
      url: this.props.url + comment.id + '/',
      dataType: 'json',
      type: 'DELETE',
      success: this.updateStateComment.bind(this, index, parentIndex),
      error: function (xhr, status, err) {
        console.error(this.props.url + comment.id + '/', status, err.toString())
      }.bind(this)
    })
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
      login_url: this.props.login_url,
      comments_contenttype: this.props.comments_contenttype,
      user_name: this.props.user_name,
      language: this.props.language
    }
  },
  render: function () {
    return (
    h('div', [
      h('div.black-divider',
        this.state.comments.length + ' ' + django.ngettext('comment', 'comments', this.state.comments.length)),
      h('div.commentBox', [
        h(CommentForm, {
          subjectType: this.props.subjectType,
          subjectId: this.props.subjectId,
          onCommentSubmit: this.handleCommentSubmit,
          placeholder: django.gettext('Your comment here'),
          rows: 5
        }),
        h('div.comment-list', [
          h(CommentList, {
            comments: this.state.comments,
            handleCommentDelete: this.handleCommentDelete,
            handleCommentSubmit: this.handleCommentSubmit,
            handleCommentModify: this.handleCommentModify
          })
        ])
      ])
    ])
    )
  }
})

CommentBox.childContextTypes = {
  isAuthenticated: React.PropTypes.number,
  login_url: React.PropTypes.string,
  comments_contenttype: React.PropTypes.number,
  user_name: React.PropTypes.string,
  language: React.PropTypes.string
}

var CommentList = React.createClass({
  render: function () {
    return (
    h('div', [
      this.props.comments.map(function (comment, index) {
        return (
        h(Comment, {
          key: comment.id,
          user_name: comment.user_name,
          child_comments: comment.child_comments,
          created: comment.created,
          modified: comment.modified,
          id: comment.id,
          content_type: comment.content_type,
          is_deleted: comment.is_deleted,
          index: index,
          parentIndex: this.props.parentIndex,
          handleCommentDelete: this.props.handleCommentDelete,
          handleCommentSubmit: this.props.handleCommentSubmit,
          handleCommentModify: this.props.handleCommentModify
        },
          comment.comment
        )
        )
      }.bind(this))
    ])
    )
  }
})

var markdown2html = function (text) {
  var rawMarkup = marked(text.toString(), {sanitize: true})
  return { __html: rawMarkup }
}

var Comment = React.createClass({

  getInitialState: function () {
    return {
      edit: false,
      showChildComments: false
    }
  },

  toggleEdit: function (e) {
    if (e) {
      e.preventDefault()
    }
    var newEdit = !this.state.edit
    this.setState({edit: newEdit})
  },

  showComments: function (e) {
    e.preventDefault()
    var newShowChildComment = !this.state.showChildComments
    this.setState({showChildComments: newShowChildComment})
  },

  allowForm: function () {
    return !(this.props.content_type === this.context.comments_contenttype)
  },

  allowRate: function () {
    return !(this.state.is_deleted)
  },

  rateUp: function (e) {
    e.preventDefault()
    console.log('+1')
  },

  rateDown: function (e) {
    e.preventDefault()
    console.log('-1')
  },

  isOwner: function () {
    return this.props.user_name === this.context.user_name
  },

  onReport: function (e) {
    e.preventDefault()
    console.log('clicked report')
  },

  render: function () {
    return (
    h('div.comment', [
      this.isOwner() ? h(Modal, {
        name: 'comment_delete_' + this.props.id,
        question: django.gettext('Do you really want to delete this comment?'),
        handler: function () {
          this.props.handleCommentDelete(this.props.index, this.props.parentIndex)
        }.bind(this),
        action: django.gettext('Delete'),
        abort: django.gettext('Abort'),
        btnStyle: 'cta'
      }) : null,
      h('h3.' + (this.props.is_deleted ? 'commentDeletedAuthor' : 'commentAuthor'), this.props.user_name),
      this.state.edit
        ? h(CommentEditForm, {
          comment: this.props.children,
          rows: 5,
          handleCancel: this.toggleEdit,
          onCommentSubmit: function (newComment) {
            this.props.handleCommentModify(newComment.comment, this.props.index, this.props.parentIndex)
            this.state.edit = false
          }.bind(this)
        })
        : h('span.comment-text', {
          dangerouslySetInnerHTML: markdown2html(this.props.children)
        }
      ),
      h('ul.nav.nav-pills', [
        h('li.entry',
          [
            this.props.modified === null
              ? h('a.commentSubmissionDate.dark',
                  moment(this.props.created).format('D MMM YY'))
              : h('a.commentSubmissionDate.dark',
                  django.gettext('Latest edit') + ' ' + moment(this.props.modified).fromNow())
          ]
        ),

        /*
        this.allowForm() ? h('li.entry', [
          h('a.icon.fa-comment-o.dark', {
            href: '#',
            onClick: this.showComments,
            'aria-hidden': true
          }, this.props.child_comments.length
          )
        ]) : null,
        */

        this.allowRate() ? h('li.entry', [
          h('a.icon.fa-chevron-up.green', {
            href: '#',
            onClick: this.rateUp,
            'aria-hidden': true
          }, this.props.child_comments.length
          )
        ]) : null,
        this.allowRate() ? h('li.entry', [
          h('a.icon.fa-chevron-down.red', {
            href: '#',
            onClick: this.rateDown,
            'aria-hidden': true
          }, this.props.child_comments.length
          )
        ]) : null,
        this.context.isAuthenticated && !this.state.is_deleted ? h('li.dropdown', {role: 'presentation'}, [
          h('a.dropdown-toggle.icon.fa-ellipsis-h.dark', {
            'data-toggle': 'dropdown',
            href: '#',
            role: 'button',
            'aria-haspopup': true,
            'aria-expanded': false,
            'aria-hidden': true
          }),
          h('ul.dropdown-menu', [].concat(
            this.isOwner() ? [ h('li', [
              h('a', {
                href: '#',
                onClick: this.toggleEdit,
                'aria-hidden': true
              }, django.gettext('Edit')
              )
            ]),
            h('li.divider'),
            h('li', [
              h('a', {
                href: '#',
                'data-toggle': 'modal',
                'data-target': '#comment_delete_' + this.props.id,
                'aria-hidden': true
              }, django.gettext('Delete'))
            ]),
            h('li.divider')] : [],
            [h('li', [
              h('a', {
                href: '#',
                onClick: this.onReport,
                'aria-hidden': true
              }, django.gettext('Report')
              )
            ])
          ]))
        ]) : null
      ]),
      !this.state.is_deleted ? h('ul.nav.nav-pills.pull-right', [
        this.allowForm() ? h('li.entry', [
          h('a.icon.fa-reply.dark', {
            href: '#',
            onClick: this.showComments,
            'aria-hidden': true
          }, django.gettext('Anwser')
          )
        ]) : null
      ]) : null,
      this.state.showChildComments ? h('div.child_comments_list', [
        h(CommentList, {
          comments: this.props.child_comments,
          parentIndex: this.props.index,
          handleCommentDelete: this.props.handleCommentDelete,
          handleCommentModify: this.props.handleCommentModify
        }),
        h(CommentForm, {
          subjectType: this.context.comments_contenttype,
          subjectId: this.props.id,
          onCommentSubmit: this.props.handleCommentSubmit,
          parentIndex: this.props.index,
          placeholder: django.gettext('Your reply here'),
          rows: 3
        })
      ]) : null
    ])
    )
  }
})

var Modal = React.createClass({
  'render': function () {
    return h('div.modal.fade#' + this.props.name, { tabindex: '-1', role: 'dialog', 'aria-labelledby': 'myModalLabel' }, [
      h('div.modal-dialog', { role: 'document' }, [
        h('div.modal-content', [
          h('div.modal-header', [
            h('button.close', {
              type: 'button',
              'data-dismiss': 'modal',
              'aria-label': this.props.abort
            }, [
              h('i.fa.fa-times', {
                'aria-hidden': true
              })
            ])
          ]),
          h('div.modal-body', [
            h('h3.modal-title', this.props.question)
          ]),
          h('div.modal-footer', [
            h('div.row', [
              h('button.btn.btn-' + (this.props.btnStyle || 'primary'),
                {
                  type: 'button',
                  'data-dismiss': 'modal',
                  onClick: this.props.handler
                },
                this.props.action)
            ]),
            h('div.row', [
              h('button.btn', {
                type: 'button',
                'data-dismiss': 'modal'
              }, this.props.abort)
            ])
          ])
        ])
      ])
    ])
  }
})

Comment.contextTypes = {
  comments_contenttype: React.PropTypes.number,
  isAuthenticated: React.PropTypes.number,
  user_name: React.PropTypes.string
}

var CommentForm = React.createClass({
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

CommentForm.contextTypes = {
  isAuthenticated: React.PropTypes.number,
  login_url: React.PropTypes.string
}

var CommentEditForm = React.createClass({
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
        value: django.gettext('cancle'),
        onClick: this.props.handleCancel
      })
    ])
    )
  }
})

CommentEditForm.contextTypes = {
  isAuthenticated: React.PropTypes.number,
  login_url: React.PropTypes.string
}

module.exports.renderComment = function (url, subjectType, subjectId, commentsContenttype, isAuthenticated, loginUrl, target, userName, language) {
  ReactDOM.render(
    h(CommentBox, {
      url: url,
      subjectType: subjectType,
      subjectId: subjectId,
      comments_contenttype: commentsContenttype,
      isAuthenticated: isAuthenticated,
      login_url: loginUrl,
      pollInterval: 20000,
      user_name: userName,
      language: language
    }),
    document.getElementById(target))
}
