/* global location */

import 'bootstrap' // load bootstrap components

import './euth_wagtail'

function init () {
}

document.addEventListener('DOMContentLoaded', init, false)

export function getCurrentPath () {
  return location.pathname
}
