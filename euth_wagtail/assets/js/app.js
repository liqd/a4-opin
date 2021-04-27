/* global location */

import 'bootstrap' // load bootstrap components

import './euth_wagtail'

// expose react components
import {
  commentsAsync as ReactCommentsAsync,
  polls as ReactPolls,
  ratings as ReactRatings,
  widget as ReactWidget
} from 'adhocracy4'

import * as ReactParagraphs from '../../../euth/documents/static/documents/ParagraphBox.jsx'
import * as ReactFollows from '../../../euth/follows/static/follows/react_follows.jsx'
import * as ReactLanguageSwitch from '../../../euth/dashboard/static/language_switch/react_language_switch.jsx'
import * as ReactUserList from '../../../euth/dashboard/static/user_list/react_user_list.jsx'

function init () {
  ReactWidget.initialise('a4', 'comment_async', ReactCommentsAsync.renderComment)
  ReactWidget.initialise('a4', 'ratings', ReactRatings.renderRatings)
  ReactWidget.initialise('a4', 'polls', ReactPolls.renderPolls)
  ReactWidget.initialise('a4', 'poll-management', ReactPolls.renderPollManagement)

  ReactWidget.initialise('euth', 'document', ReactParagraphs.renderParagraphs)
  ReactWidget.initialise('euth', 'follows', ReactFollows.renderFollow)
  ReactWidget.initialise('euth', 'userlist', ReactUserList.renderUserList)
  ReactWidget.initialise('euth', 'language-switch', ReactLanguageSwitch.renderLanguageSwitch)
}

document.addEventListener('DOMContentLoaded', init, false)

export function getCurrentPath () {
  return location.pathname
}

// enabling bootstrap popovers
$(function () {
  $('[data-toggle="popover"]').popover()
})
