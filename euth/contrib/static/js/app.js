/* global location */

var widget = require('adhocracy4').widget
var ReactComments = require('adhocracy4').comments
var ReactParagraphs = require('../../../documents/static/documents/ParagraphBox.jsx')
var ReactPolls = require('adhocracy4').polls
var ReactRatings = require('adhocracy4').ratings
var ReactFollow = require('../../../follows/static/follows/react_follows.jsx')
var ReactLanguageSwitch = require('../../../dashboard/static/language_switch/react_language_switch.jsx')
var ReactUserList = require('../../../dashboard/static/user_list/react_user_list.jsx')
var $ = window.jQuery = window.$ = require('jquery')

require('../../../../euth_wagtail/assets/js/euth_wagtail')

var getCurrentPath = function () {
  return location.pathname
}

$(function () {
  widget.initialise('a4', 'comment', ReactComments.renderComment)
  widget.initialise('a4', 'ratings', ReactRatings.renderRatings)
  widget.initialise('a4', 'polls', ReactPolls.renderPolls)
  widget.initialise('a4', 'poll-management', ReactPolls.renderPollManagement)
  widget.initialise('euth', 'document', ReactParagraphs.renderParagraphs)
  widget.initialise('euth', 'follows', ReactFollow.renderFollow)
  widget.initialise('euth', 'userlist', ReactUserList.renderUserList)
  widget.initialise('euth', 'language-switch', ReactLanguageSwitch.renderLanguageSwitch)
})

module.exports = {
  getCurrentPath: getCurrentPath
}
