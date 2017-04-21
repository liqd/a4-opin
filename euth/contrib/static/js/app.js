var moment = require('moment')
var ReactComments = require('adhocracy4').comments
var ReactParagraphs = require('../../../documents/static/documents/ParagraphBox.jsx')
var ReactRatings = require('adhocracy4').ratings
var ReactFollow = require('../../../follows/static/follows/react_follows.jsx')
var ReactLanguageSwitch = require('../../../dashboard/static/language_switch/react_language_switch.jsx')
var ReactUserList = require('../../../dashboard/static/user_list/react_user_list.jsx')

require('../../../../euth_wagtail/assets/js/euth_wagtail')

module.exports = {
  'renderComment': ReactComments.renderComment,
  'renderRatings': ReactRatings.renderRatings,
  'renderLanguageSwitch': ReactLanguageSwitch.renderLanguageSwitch,
  'renderParagraphs': ReactParagraphs.renderParagraphs,
  'renderFollow': ReactFollow.renderFollow,
  'renderUserList': ReactUserList.renderUserList
}

moment.locale(document.documentElement.lang)

var initialiseWidget = function (project, name, initialiser) {
  if (!initialiser) {
    initialiser = name
    name = project
    project = 'euth'
  }

  document.addEventListener('DOMContentLoaded', function () {
    var els = document.querySelectorAll('[data-' + project + '-widget=\'' + name + '\']')

    for (var i in els) {
      if (els.hasOwnProperty(i)) {
        initialiser(els[i])
      }
    }
  })
}

initialiseWidget('document', ReactParagraphs.renderParagraphs)
initialiseWidget('follows', ReactFollow.renderFollow)
initialiseWidget('userlist', ReactUserList.renderUserList)
initialiseWidget('language-switch', ReactLanguageSwitch.renderLanguageSwitch)
