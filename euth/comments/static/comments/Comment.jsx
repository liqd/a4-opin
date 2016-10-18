var Report = require('../../../../euth/reports/static/reports/react_reports')
var Ratings = require('../../../../euth/ratings/static/ratings/react_ratings')
var Modal = require('../../../contrib/static/js/Modal')
var CommentEditForm = require('./CommentEditForm')
var CommentList = require('./CommentList')
var CommentForm = require('./CommentForm')

var React = require('react')
var h = require('react-hyperscript')
var django = require('django')
var moment = require('moment')
var marked = require('marked')

var markdown2html = function (text) {
  var rawMarkup = marked(text.toString(), {sanitize: true})
  return { __html: rawMarkup }
}

module.exports.Comment = React.createClass({
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

        this.isOwner() || this.context.isModerator ? h(Modal, {
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
        this.state.edit ? h(CommentEditForm, {
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
                  ? h('span.commentSubmissionDate',
                  moment(this.props.created).format('D MMM YY'))
                  : h('span.commentSubmissionDate',
                  django.gettext('Latest edit') + ' ' + moment(this.props.modified).fromNow())
              ])
            ]),

            !this.props.is_deleted ? h(Ratings.RatingBox, {
              url: this.context.ratingsUrls,
              loginUrl: this.context.login_url,
              contentType: this.context.comments_contenttype,
              objectId: this.props.id,
              authenticatedAs: this.context.isAuthenticated ? this.context.user_name : null,
              pollInterval: 20000,
              style: 'comments',
              positiveRatings: this.props.positiveRatings,
              negativeRatings: this.props.negativeRatings,
              userRating: this.props.userRating,
              userRatingId: this.props.userRatingId,
              isReadOnly: this.props.isReadOnly
            }) : null,

            h('ul.nav.navbar-nav', [

              this.context.isAuthenticated && !this.props.is_deleted ? h('li.dropdown', {role: 'presentation'}, [
                h('a.dropdown-toggle.icon.fa-ellipsis-h', {
                  'data-toggle': 'dropdown',
                  href: '#',
                  role: 'button',
                  'aria-haspopup': true,
                  'aria-expanded': false,
                  'aria-hidden': true
                }),

                h('ul.dropdown-menu', [].concat(
                  (this.isOwner() || this.context.isModerator) && !this.props.isReadOnly ? [h('li', [
                    h('a', {
                      href: '#',
                      onClick: this.toggleEdit,
                      'aria-hidden': true
                    }, django.gettext('Edit'))
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
                    }, django.gettext('Report'))
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
                h('a.icon.fa-reply', {
                  href: '#',
                  onClick: this.showComments,
                  'aria-hidden': true
                }, django.gettext('Answer'))
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
module.exports.Comment.contextTypes = {
  comments_contenttype: React.PropTypes.number,
  isAuthenticated: React.PropTypes.bool,
  isModerator: React.PropTypes.bool,
  user_name: React.PropTypes.string,
  login_url: React.PropTypes.string,
  ratingsUrls: React.PropTypes.string,
  contentType: React.PropTypes.number
}
