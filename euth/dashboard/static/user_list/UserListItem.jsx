var React = require('react')

var UserListItem = function (props) {
  return (
    <tr>
      <td>
        <a href={`/profile/${props.user.username}`}>
          <Avatar src={props.user.avatar} fallback={props.user.default_avatar} /> {props.user.username}
        </a>
      </td>
      <td>
        {props.user.email}
      </td>
      <td>
        <input type="checkbox" name={`user_${props.user.id}`}
          id={`user_${props.user.id}`} data-userid={props.user.id} />
      </td>
    </tr>
  )
}

UserListItem.propTypes = {
  user: React.PropTypes.object
}

var Avatar = function (props) {
  let avatar = props.src ? props.src : props.fallback
  return <img src={avatar} alt="" className="circled" />
}

Avatar.propTypes = {
  src: React.PropTypes.string,
  fallback: React.PropTypes.string
}

module.exports = UserListItem
