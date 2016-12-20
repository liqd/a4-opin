var api = require('../../../contrib/static/js/api')
var django = require('django')
var React = require('react')

var FollowButton = React.createClass({
  getInitialState: function () {
    return {
      followed: undefined
    }
  },
  toggleFollow: function () {
    api.follow.change({ enabled: !this.state.followed }, this.props.project)
       .done((follow) => {
         this.setState({
           followed: follow.enabled
         })
       })
  },
  componentDidMount: function () {
    api.follow.get(this.props.project)
       .done((follow) => {
         this.setState({
           followed: follow.enabled
         })
       })
       .fail((response) => {
         response.status === 404
         this.setState({
           followed: false
         })
       })
  },
  render: function () {
    return (
      <span>
        <button className="btn btn-sm btn-dark btn-primary" type="button" onClick={this.toggleFollow}>
          <i className={this.state.followed ? 'fa fa-star' : 'fa fa-star-o'} aria-hidden="true" />
          &nbsp;{this.state.followed ? django.gettext('Unfollow') : django.gettext('Follow')}
        </button>
      </span>
    )
  }
})

module.exports = FollowButton
