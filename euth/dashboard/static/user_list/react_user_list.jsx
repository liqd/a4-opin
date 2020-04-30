var $ = require('jquery')
var cookie = require('js-cookie')
var django = require('django')
var PropTypes = require('prop-types')
var React = require('react')
var ReactDOM = require('react-dom')
var UserListItem = require('./UserListItem.jsx')

$(function () {
  $.ajaxSetup({
    headers: { 'X-CSRFToken': cookie.get('csrftoken') }
  })
})

class UserList extends React.Component {
  constructor (props) {
    super(props)

    this.state = {
      users: props.users,
      listenTo: props.listenTo
    }
  }

  add (user) {
    // create new array with only user IDs and add the new one
    const users = this.state.users.concat([user])

    return this.updateUsers(users, this.props.project)
  }

  updateUsers (users, projectId) {
    users = users.map(user => user.id)

    return $.ajax({
      type: 'PATCH',
      url: `/api/projects/${projectId}/`,
      data: JSON.stringify({ moderators: users }),
      dataType: 'json',
      contentType: 'application/json; charset=utf-8'
    }).done(data => {
      this.setState({
        users: data[this.props.listenTo]
      })
    })
  }

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
    this.updateUsers(users, this.props.project)
  }

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
        <button type="button" className="btn btn-danger" onClick={this.submitHandler.bind(this)} value="remove">
          {django.gettext('Remove')}
        </button>
      </div>
    )
  }
}

UserList.propTypes = {
  users: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number,
      username: PropTypes.string,
      email: PropTypes.string,
      avatar: PropTypes.string,
      avatar_fallback: PropTypes.string
    })
  ),
  listenTo: PropTypes.string,
  project: PropTypes.number
}

UserList.defaultProps = {
  users: []
}

module.exports.renderUserList = function (el) {
  const users = JSON.parse(el.getAttribute('data-users'))
  const listenTo = $(el).data('listen-to')
  const project = $(el).data('project')

  // check if userList object exists, otherwise create an empty one
  window.adhocracy4.userList = window.adhocracy4.userList || {}
  window.adhocracy4.userList[listenTo] = window.adhocracy4.userList[listenTo] || []
  // add just created React component to the object
  window.adhocracy4.userList[listenTo].push(
    ReactDOM.render(
      <UserList users={users} listenTo={listenTo} project={project} />,
      el
    )
  )
}
