const React = require('react')
const PropTypes = require('prop-types')

const UserListItem = function (props) {
  return (
    <tr>
      <td>
        <a href={`/profile/${props.user.username}`}>
          <Avatar src={props.user.avatar} fallback={props.user.avatar_fallback} /> {props.user.username}
        </a>
      </td>
      <td>
        {props.user.email}
      </td>
      <td>
        <input
          type="checkbox" name={`user_${props.user.id}`}
          id={`user_${props.user.id}`} data-userid={props.user.id}
        />
      </td>
    </tr>
  )
}

UserListItem.propTypes = {
  user: PropTypes.object
}

const Avatar = function (props) {
  const avatar = props.src ? props.src : props.fallback
  return <img src={avatar} alt="" className="circled" />
}

Avatar.propTypes = {
  src: PropTypes.string,
  fallback: PropTypes.string
}

module.exports = UserListItem
