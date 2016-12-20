var ReactComments = require('../../../comments/static/comments/react_comments.jsx')
var ReactParagraphs = require('../../../documents/static/documents/ParagraphBox.jsx')
var ReactRatings = require('../../../ratings/static/ratings/react_ratings.jsx')
var ReactFollow = require('../../../follows/static/follows/react_follows.jsx')
var ReactLanguageSwitch = require('../../../dashboard/static/language_switch/react_language_switch.jsx')
require('../../../../euth_wagtail/assets/js/euth_wagtail')
require('../../../../euth_wagtail/assets/js/highcharts/highcharts')
require('../../../../euth_wagtail/assets/js/highcharts/highcharts.src')
require('../../../../euth_wagtail/assets/js/highcharts/highcharts-more')
require('../../../../euth_wagtail/assets/js/highcharts/highmaps')
require('../../../../euth_wagtail/assets/js/highcharts/highstock')
require('../../../../euth_wagtail/assets/js/highcharts/map')

module.exports = {
  'renderComment': ReactComments.renderComment,
  'renderRatings': ReactRatings.renderRatings,
  'renderLanguageSwitch': ReactLanguageSwitch.renderLanguageSwitch,
  'renderParagraphs': ReactParagraphs.renderParagraphs,
  'renderFollow': ReactFollow.renderFollow
}
