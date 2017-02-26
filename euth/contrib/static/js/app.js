var ReactComments = require('adhocracy4').comments
var ReactParagraphs = require('../../../documents/static/documents/ParagraphBox.jsx')
var ReactRatings = require('adhocracy4').ratings
var ReactFollow = require('../../../follows/static/follows/react_follows.jsx')
var ReactLanguageSwitch = require('../../../dashboard/static/language_switch/react_language_switch.jsx')
var ReactUserList = require('../../../dashboard/static/user_list/react_user_list.jsx')

require('../../../../euth_wagtail/assets/js/fp_wagtail')
require('../../../../euth_wagtail/assets/js/euth_wagtail')

module.exports = {
  'renderComment': ReactComments.renderComment,
  'renderRatings': ReactRatings.renderRatings,
  'renderLanguageSwitch': ReactLanguageSwitch.renderLanguageSwitch,
  'renderParagraphs': ReactParagraphs.renderParagraphs,
  'renderFollow': ReactFollow.renderFollow,
  'renderUserList': ReactUserList.renderUserList
}
