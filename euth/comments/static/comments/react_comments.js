var Rates = require('../../../../euth/rates/static/rates/react_rates')
var Report = require('../../../../euth/reports/static/reports/react_reports')
var api = require('../../../contrib/static/js/api')

var React = require('react')
var ReactDOM = require('react-dom')
var h = require('react-hyperscript')
var update = require('react-addons-update')
var marked = require('marked')
var moment = require('moment')
var django = require('django')

var CommentBox = React.createClass({
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
      login_url: this.props.login_url,
      ratesUrls: this.props.ratesUrls,
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
        this.props.isReadOnly ? null : h(CommentForm, {
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
            handleCommentModify: this.handleCommentModify,
            isReadOnly: this.props.isReadOnly
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
  ratesUrls: React.PropTypes.string,
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
          handleCommentModify: this.props.handleCommentModify,
          positiveRates: comment.rates.positive_rates,
          negativeRates: comment.rates.negative_rates,
          userRate: comment.rates.current_user_rate_value,
          userRateId: comment.rates.current_user_rate_id,
          isReadOnly: this.props.isReadOnly
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
    return !this.props.isReadOnly && this.props.content_type !== this.context.comments_contenttype
  },

  isOwner: function () {
    return this.props.user_name === this.context.user_name
  },

  pluralizeString: function (number) {
    var fmts = django.ngettext('view %s reply',
        'view %s replies', number)
    var s = django.interpolate(fmts, [number])
    return s
  },

  render: function () {
    return (
    h('div.comment', [

      h(Report.ReportModal, {
        name: 'report_comment_' + this.props.id,
        title: django.gettext('Are you sure you want to report this item?'),
        btnStyle: 'cta',
        objectId: this.props.id,
        contentType: this.context.comments_contenttype
      }),

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

        : h('div.comment-text', {
          dangerouslySetInnerHTML: markdown2html(this.props.children)
        }
      ),

      h('div.action-bar', [

        h('nav.navbar.navbar-default.navbar-static', [

          h('ul.nav.navbar-nav', [
            h('li.entry', [
              this.props.modified === null
                ? h('a.commentSubmissionDate.dark',
                    moment(this.props.created).format('D MMM YY'))
                : h('a.commentSubmissionDate.dark',
                    django.gettext('Latest edit') + ' ' + moment(this.props.modified).fromNow())
            ])
          ]),

          !this.props.is_deleted ? h(Rates.RateBox, {
            url: this.context.ratesUrls,
            loginUrl: this.context.login_url,
            contentType: this.context.comments_contenttype,
            objectId: this.props.id,
            authenticatedAs: this.context.isAuthenticated ? this.context.user_name : null,
            pollInterval: 20000,
            style: 'comments',
            positiveRates: this.props.positiveRates,
            negativeRates: this.props.negativeRates,
            userRate: this.props.userRate,
            userRateId: this.props.userRateId,
            isReadOnly: this.props.isReadOnly
          }) : null,

          h('ul.nav.navbar-nav', [

            this.context.isAuthenticated && !this.props.is_deleted ? h('li.dropdown', {role: 'presentation'}, [
              h('a.dropdown-toggle.icon.fa-ellipsis-h.dark', {
                'data-toggle': 'dropdown',
                href: '#',
                role: 'button',
                'aria-haspopup': true,
                'aria-expanded': false,
                'aria-hidden': true
              }),

              h('ul.dropdown-menu', [].concat(
                this.isOwner() && !this.props.isReadOnly ? [ h('li', [
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
                    'data-toggle': 'modal',
                    'data-target': '#report_comment_' + this.props.id,
                    'aria-hidden': true
                  }, django.gettext('Report')
                  )
                ])
              ]))

            ]) : null // end li.dropdown

          ])
        ])
      ]),

      !this.props.is_deleted ? h('div.action-bar', [

        h('nav.navbar.navbar-default.navbar-static', [
          this.props.child_comments.length > 0 ? h('ul.nav.navbar-nav', [
            h('li', [
              h('a', {
                href: '#',
                onClick: this.showComments
              }, this.pluralizeString(this.props.child_comments.length))
            ])
          ]) : null,

          h('ul.nav.navbar-nav.navbar-right', [
            this.allowForm() ? h('li.entry', [
              h('a.icon.fa-reply.dark', {
                href: '#',
                onClick: this.showComments,
                'aria-hidden': true
              }, django.gettext('Answer')
              )
            ]) : null
          ])
        ])
      ]) : null, // end div.action-bar

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
      ]) : null // end div.child_comments_list

    ])
    )
  }
})

var Modal = React.createClass({
  'render': function () {
    return h('div.modal.fade#' + this.props.name, { tabindex: '-1', role: 'dialog', 'aria-labelledby': 'myModalLabel' }, [
      h('div.modal-dialog.modal-lg', { role: 'document' }, [
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
              h('button.submit-button',
                {
                  type: 'button',
                  'data-dismiss': 'modal',
                  onClick: this.props.handler
                },
                this.props.action)
            ]),
            h('div.row', [
              h('button.cancel-button', {
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
  user_name: React.PropTypes.string,
  login_url: React.PropTypes.string,
  ratesUrls: React.PropTypes.string,
  contentType: React.PropTypes.number
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
        value: django.gettext('cancel'),
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

module.exports.renderComment = function (url, ratesUrls, subjectType, subjectId, commentsContenttype, isAuthenticated, loginUrl, target, userName, language, isReadOnly) {
  ReactDOM.render(
    h(CommentBox, {
      url: url,
      ratesUrls: ratesUrls,
      subjectType: subjectType,
      subjectId: subjectId,
      comments_contenttype: commentsContenttype,
      isAuthenticated: isAuthenticated,
      login_url: loginUrl,
      pollInterval: 20000,
      user_name: userName,
      language: language,
      isReadOnly: isReadOnly
    }),
    document.getElementById(target))
}
