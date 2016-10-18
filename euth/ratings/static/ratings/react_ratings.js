var api = require('../../../contrib/static/js/api')
var config = require('../../../contrib/static/js/config')

var React = require('react')
var ReactDOM = require('react-dom')
var h = require('react-hyperscript')
var django = require('django')

var RatingBox = React.createClass({
  handleRatingCreate: function (number) {
    api.rating.add({
      object_pk: this.props.objectId,
      content_type: this.props.contentType,
      value: number
    }).done(function (data) {
      this.setState({
        positiveRatings: data.meta_info.positive_ratings_on_same_object,
        negativeRatings: data.meta_info.negative_ratings_on_same_object,
        userRating: data.meta_info.user_rating_on_same_object_value,
        userHasRatingd: true,
        userRatingId: data.id
      })
    }.bind(this))
  },
  handleRatingModify: function (number, id) {
    api.rating.change({value: number}, id)
      .done(function (data) {
        this.setState({
          positiveRatings: data.meta_info.positive_ratings_on_same_object,
          negativeRatings: data.meta_info.negative_ratings_on_same_object,
          userRating: data.meta_info.user_rating_on_same_object_value
        })
      }.bind(this))
  },
  updateUserRating: function (data) {
    this.state.ratings[this.state.userRatingIndex] = data
  },
  ratingUp: function (e) {
    e.preventDefault()
    if (this.props.auhenticatedAs === null) {
      window.location.href = config.login
      return
    }
    if (this.props.isReadOnly) {
      return
    }
    if (this.state.userHasRatingd) {
      var number
      if (this.state.userRating === 1) {
        number = 0
      } else {
        number = 1
      }
      this.handleRatingModify(number, this.state.userRatingId)
    } else {
      this.handleRatingCreate(1)
    }
  },
  ratingDown: function (e) {
    e.preventDefault()
    if (this.props.authenticatedAs === null) {
      window.location.href = django.urls.login()
      return
    }
    if (this.props.isReadOnly) {
      return
    }
    if (this.state.userHasRatingd) {
      var number
      if (this.state.userRating === -1) {
        number = 0
      } else {
        number = -1
      }
      this.handleRatingModify(number, this.state.userRatingId)
    } else {
      this.handleRatingCreate(-1)
    }
  },
  getInitialState: function () {
    return {
      positiveRatings: this.props.positiveRatings,
      negativeRatings: this.props.negativeRatings,
      userHasRatingd: this.props.userRating !== null,
      userRating: this.props.userRating,
      userRatingId: this.props.userRatingId
    }
  },
  componentDidMount: function () {
    this.getInitialState()
  },
  render: function () {
    if (this.props.style === 'comments') {
      return (
        h('ul.nav.navbar-nav', [
          h('li.entry', [
            h('a.icon.fa-chevron-up.comment-rating-up' + (this.state.userRating === 1 ? '.is-selected' : ''), {
              href: '#',
              onClick: this.ratingUp,
              'aria-hidden': true
            }, this.state.positiveRatings
          )
          ]),
          h('li.entry', [
            h('a.icon.fa-chevron-down.comment-rating-down' + (this.state.userRating === -1 ? '.is-selected' : ''), {
              href: '#',
              onClick: this.ratingDown,
              'aria-hidden': true
            }, this.state.negativeRatings
            )
          ])
        ])
      )
    } else {
      return (
        h('div.idea-rating', [
          h('a.idea-rating-btn.idea-rating-up' + (this.props.isReadOnly ? '.is-read-only' : '') + (this.state.userRating === 1 ? '.is-selected' : ''), {
            href: '#',
            title: 'Vote Up',
            onClick: this.ratingUp
          }, [
            h('i.fa.fa-chevron-up', [
              h('span', ' ' + this.state.positiveRatings)
            ])
          ]
          ),
          h('a.idea-rating-btn.idea-rating-down' + (this.props.isReadOnly ? '.is-read-only' : '') + (this.state.userRating === -1 ? '.is-selected' : ''), {
            href: '#',
            title: 'Vote Down',
            onClick: this.ratingDown
          }, [
            h('i.fa.fa-chevron-down', [
              h('span', ' ' + this.state.negativeRatings)
            ])
          ])
        ])
      )
    }
  }
})

module.exports.RatingBox = RatingBox

module.exports.renderRatings = function (mountpoint, props) {
  ReactDOM.render(h(RatingBox, props), document.getElementById(mountpoint))
}
