/* global projectId */
var React = require('react')
var ReactDOM = require('react-dom')
var $ = require('jquery')
var django = require('django')
var UserListItem = require('./UserListItem.jsx')

var UserList = React.createClass({
  selectedUsers: [],

  getInitialState () {
    return {
      users: this.props.users,
      listenTo: this.props.listenTo
    }
  },

  add (user) {
    // create new array with only user IDs and add the new one
    let users = this.state.users.concat([user])
    if (!projectId) {
      console.error(`projectId is ${projectId}.`)
    }

    return this.updateUsers(users)
  },

  updateUsers (users) {
    users = users.map(user => user.id)

    return $.ajax({
      type: 'PATCH',
      url: `/api/projects/${projectId}/`,
      data: JSON.stringify({moderators: users}),
      dataType: 'json',
      contentType: 'application/json; charset=utf-8'
    }).done(data => {
      this.setState({
        users: data[this.props.listenTo]
      })
    })
  },

  submitHandler (e) {
    var checkedUsers = this.refs.userlist.querySelectorAll(':checked')
    var idsToBeActedOn = Array.prototype.map.call(checkedUsers,
      user => parseInt(user.dataset.userid)
    )
    // create new array
    var users = this.state.users.concat([])
    if (e.target.value === 'remove') {
      // filter out users whose id is in idsToBeActedOn
      users = users.filter(user => idsToBeActedOn.indexOf(user.id) === -1)
    }
    this.updateUsers(users)
  },

  render () {
    var userList = this.state.users.map(user => {
      return <UserListItem key={user.id} user={user} />
    })
    return (
      <div ref="userlist">
        <table className="table table-hover">
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Edit</th>
            </tr>
          </thead>
          <tbody>
            {userList}
          </tbody>
        </table>
        <button type="button" className="btn btn-danger" onClick={this.submitHandler} value="remove">
          {django.gettext('Remove')}
        </button>
      </div>
    )
  }
})

UserList.propTypes = {
  users: React.PropTypes.array,
  listenTo: React.PropTypes.string
}
UserList.defaultProps = {
  users: []
}

module.exports.renderUserList = function (target, userArray, listenTo) {
  // check if userList object exists, otherwise create an empty one
  window.adhocracy4.userList = window.adhocracy4.userList || {}
  window.adhocracy4.userList[listenTo] = window.adhocracy4.userList[listenTo] || []
  // add just created React component to the object
  window.adhocracy4.userList[listenTo].push(
    ReactDOM.render(
      <UserList users={userArray} listenTo={listenTo} />,
      document.getElementById(target)
    )
  )
}
