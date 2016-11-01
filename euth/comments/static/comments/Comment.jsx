var ReportModal = require('../../../reports/static/reports/react_reports')
var RatingBox = require('../../../../euth/ratings/static/ratings/react_ratings').RatingBox
var Modal = require('../../../contrib/static/js/Modal')
var CommentEditForm = require('./CommentEditForm')
var CommentForm = require('./CommentForm')
var CommentReplyBar = require('./CommentReplyBar')
var CommentManageDropdown = require('./CommentManageDropdown')

var React = require('react')
var django = require('django')
var moment = require('moment')
var marked = require('marked')

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

  renderRatingBox: function () {
    if (!this.props.is_deleted) {
      return (
        <RatingBox
          contentType={this.context.comments_contenttype}
          objectId={this.props.id}
          authenticatedAs={this.context.isAuthenticated ? this.context.user_name : null}
          positiveRatings={this.props.positiveRatings}
          negativeRatings={this.props.negativeRatings}
          userRating={this.props.userRating}
          userRatingId={this.props.userRatingId}
          isReadOnly={this.props.isReadOnly}
        />
      )
    }
  },

  renderComment: function () {
    let comment
    if (this.state.edit) {
      comment = (
        <CommentEditForm
          comment={this.props.children}
          rows="5"
          handleCancel={this.toggleEdit}
          onCommentSubmit={newComment => {
            this.props.handleCommentModify(newComment.comment, this.props.index, this.props.parentIndex)
            this.state.edit = false
          }}
        />
      )
    } else {
      comment = <div className="comment-text" dangerouslySetInnerHTML={markdown2html(this.props.children)} />
    }
    return comment
  },

  renderDeleteModal: function () {
    if (this.isOwner() || this.context.isModerator) {
      return (
        <Modal
          name={`comment_delete_${this.props.id}`}
          partials={{title: django.gettext('Do you really want to delete this comment?')}}
          submitHandler={() => this.props.handleCommentDelete(this.props.index, this.props.parentIndex)}
          action={django.gettext('Delete')}
          abort={django.gettext('Abort')}
          btnStyle="cta"
        />
      )
    }
  },

  render: function () {
    var CommentList = require('./CommentList')
    let lastDate
    if (this.props.modified === null) {
      lastDate = moment(this.props.created).format('D MMM YY')
    } else {
      lastDate = django.gettext('Latest edit') + ' ' + moment(this.props.modified).fromNow()
    }

    return (
      <div className="comment">
        <ReportModal
          name={`report_comment_${this.props.id}`}
          title={django.gettext('Are you sure you want to report this item?')}
          btnStyle="cta"
          objectId={this.props.id}
          contentType={this.context.comments_contenttype}
        />
        {this.renderDeleteModal()}
        <h3 className={this.props.is_deleted ? 'comment-deleted-author' : 'comment-author'}>{this.props.user_name}</h3>
        {this.renderComment()}
        <div className="action-bar">
          <nav className="navbar navbar-default navbar-static">
            <ul className="nav navbar-nav">
              <li className="entry"><span className="comment-submission-date">{lastDate}</span></li>
            </ul>
            {this.renderRatingBox()}
            {this.context.isAuthenticated && !this.props.is_deleted &&
              <CommentManageDropdown
                id={this.props.id}
                toggleEdit={this.toggleEdit}
                renderModeratorOptions={(this.isOwner() || this.context.isModerator) && !this.props.isReadOnly}
              />
            }
          </nav>
        </div>
        <CommentReplyBar allowForm={this.allowForm()} showComments={this.showComments}
          childCommentsLength={this.props.child_comments ? this.props.child_comments.length : 0} />
        {this.state.showChildComments
          ? <div className="comment-child-list">
            <CommentList
              comments={this.props.child_comments}
              parentIndex={this.props.index}
              handleCommentDelete={this.props.handleCommentDelete}
              handleCommentModify={this.props.handleCommentModify}
            />
            <CommentForm
              subjectType={this.context.comments_contenttype}
              subjectId={this.props.id}
              onCommentSubmit={this.props.handleCommentSubmit}
              parentIndex={this.props.index}
              placeholder={django.gettext('Your reply here')}
              rows="3"
            />
          </div> : null
        }
      </div>
    )
  }
})

Comment.contextTypes = {
  comments_contenttype: React.PropTypes.number,
  isAuthenticated: React.PropTypes.bool,
  isModerator: React.PropTypes.bool,
  user_name: React.PropTypes.string,
  contentType: React.PropTypes.number
}

module.exports = Comment
