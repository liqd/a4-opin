const $ = require('jquery')
const cookie = require('js-cookie')
const django = require('django')
const PropTypes = require('prop-types')
const React = require('react')
const ReactDOM = require('react-dom')
const UserListItem = require('./UserListItem.jsx')

$(function () {
  $.ajaxSetup({
    headers: { 'X-CSRFToken': cookie.get('csrftoken') }
  })
})

class UserList extends React.Component {
  constructor (props) {
    super(props)
    this.userlistRef = React.createRef()

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
    const checkedUsers = this.userlistRef.querySelectorAll(':checked')
    const idsToBeActedOn = Array.prototype.map.call(checkedUsers,
      user => parseInt(user.dataset.userid)
    )
    // create new array
    let users = this.state.users.concat([])
    if (e.target.value === 'remove') {
      // filter out users whose id is in idsToBeActedOn
      users = users.filter(user => idsToBeActedOn.indexOf(user.id) === -1)
    }
    this.updateUsers(users, this.props.project)
  }

  render () {
    const userList = this.state.users.map(user => {
      return <UserListItem key={user.id} user={user} />
    })
    return (
      <div ref={this.userlistRef}>
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
