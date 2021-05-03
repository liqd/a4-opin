const api = require('adhocracy4').api
const django = require('django')
const PropTypes = require('prop-types')
const React = require('react')

class FollowButton extends React.Component {
  constructor (props) {
    super(props)

    this.state = {
      followed: undefined,
      follows: 0
    }
  }

  toggleFollow () {
    api.follow.change({ enabled: !this.state.followed }, this.props.project)
      .done((follow) => {
        this.setState({
          followed: follow.enabled,
          follows: follow.follows
        })
      })
  }

  componentDidMount () {
    api.follow.get(this.props.project)
      .done((follow) => {
        this.setState({
          followed: follow.enabled,
          follows: follow.follows
        })
      })
      .fail((response) => {
        if (response.status === 404) {
          this.setState({
            followed: false
          })
        }
      })
  }

  render () {
    return (
      <span className="btngroup btngroup-gray">
        <button className="btn btn-sm btn-dark btn-primary" type="button" onClick={this.toggleFollow.bind(this)}>
          <i className={this.state.followed ? 'fas fa-star' : 'far fa-star'} aria-hidden="true" />
          &nbsp;{this.state.followed ? django.gettext('Unfollow') : django.gettext('Follow')}
        </button>
        <span className="btn btn-sm btn-dark btn-primary">{this.state.follows}</span>
      </span>
    )
  }
}

FollowButton.propTypes = {
  project: PropTypes.string.isRequired
}

module.exports = FollowButton
