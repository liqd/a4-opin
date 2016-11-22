var FollowButton = require('./FollowButton')
var React = require('react')
var ReactDOM = require('react-dom')

module.exports.renderFollow = function (mountpoint, props) {
  ReactDOM.render(<FollowButton {...props} />, document.getElementById(mountpoint))
}
