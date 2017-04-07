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

var initilizeWidget = function (project, name, initializer) {
  if (!initializer) {
    initializer = name
    name = project
    project = 'euth'
  }

  document.addEventListener('DOMContentLoaded', function () {
    var els = document.querySelectorAll('[data-' + project + '-widget=\'' + name + '\']')

    for (var i in els) {
      if (els.hasOwnProperty(i)) {
        initializer(els[i])
      }
    }
  })
}

initilizeWidget('document', ReactParagraphs.renderParagraphs)
initilizeWidget('follows', ReactFollow.renderFollow)
