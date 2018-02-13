var widget = require('adhocracy4').widget
var ReactComments = require('adhocracy4').comments
var ReactParagraphs = require('../../../documents/static/documents/ParagraphBox.jsx')
var ReactRatings = require('adhocracy4').ratings
var ReactFollow = require('../../../follows/static/follows/react_follows.jsx')
var ReactLanguageSwitch = require('../../../dashboard/static/language_switch/react_language_switch.jsx')
var $ = window.jQuery = window.$ = require('jquery')

require('../../../../euth_wagtail/static/js/euth_wagtail')

$(function () {
  widget.initialise('a4', 'comment', ReactComments.renderComment)
  widget.initialise('a4', 'ratings', ReactRatings.renderRatings)
  widget.initialise('euth', 'document', ReactParagraphs.renderParagraphs)
  widget.initialise('euth', 'follows', ReactFollow.renderFollow)
  widget.initialise('euth', 'language-switch', ReactLanguageSwitch.renderLanguageSwitch)
})
