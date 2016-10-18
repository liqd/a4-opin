var CommentBox = require('./CommentBox')

var ReactDOM = require('react-dom')
var h = require('react-hyperscript')

module.exports.renderComment = function (url, ratingsUrls, subjectType, subjectId, commentsContenttype, isAuthenticated, isModerator, loginUrl, target, userName, language, isReadOnly) {
  ReactDOM.render(
    h(CommentBox, {
      url: url,
      ratingsUrls: ratingsUrls,
      subjectType: subjectType,
      subjectId: subjectId,
      comments_contenttype: commentsContenttype,
      isAuthenticated: isAuthenticated,
      isModerator: isModerator,
      login_url: loginUrl,
      pollInterval: 20000,
      user_name: userName,
      language: language,
      isReadOnly: isReadOnly
    }),
    document.getElementById(target))
}
