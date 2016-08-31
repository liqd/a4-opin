var $ = require('jquery')
var React = require('react')
var ReactDOM = require('react-dom')
var h = require('react-hyperscript')
var cookie = require('js-cookie')

$(function () {
  $.ajaxSetup({
    headers: { 'X-CSRFToken': cookie.get('csrftoken') }
  })
})

var RateBox = React.createClass({
  handleRateCreate: function (number) {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: {
        object_pk: this.props.objectId,
        content_type: this.props.contentType,
        value: number
      },
      success: function (data) {
        this.setState({
          positiveRates: data.meta_info.positive_rates_on_same_object,
          negativeRates: data.meta_info.negative_rates_on_same_object,
          userRate: data.meta_info.user_rate_on_same_object_value,
          userHasRated: true,
          userRateId: data.id
        })
      }.bind(this),
      error: function (xhr, status, err) {
        console.error(status, err.toString())
      }
    })
  },
  handleRateModify: function (number, id) {
    $.ajax({
      url: this.props.url + id + '/',
      dataType: 'json',
      type: 'PATCH',
      data: { value: number },
      success: function (data) {
        this.setState({
          positiveRates: data.meta_info.positive_rates_on_same_object,
          negativeRates: data.meta_info.negative_rates_on_same_object,
          userRate: data.meta_info.user_rate_on_same_object_value
        })
      }.bind(this),
      error: function (xhr, status, err) {
        console.error(status, err.toString())
      }
    })
  },
  updateUserRate: function (data) {
    this.state.rates[this.state.userRateIndex] = data
  },
  rateUp: function (e) {
    e.preventDefault()
    if (this.props.authenticatedAs === null) {
      window.location.href = this.props.loginUrl
      return
    }
    if (this.props.isReadOnly) {
      return
    }
    if (this.state.userHasRated) {
      var number
      if (this.state.userRate === 1) {
        number = 0
      } else {
        number = 1
      }
      this.handleRateModify(number, this.state.userRateId)
    } else {
      this.handleRateCreate(1)
    }
  },
  rateDown: function (e) {
    e.preventDefault()
    if (this.props.authenticatedAs === null) {
      window.location.href = this.props.loginUrl
      return
    }
    if (this.props.isReadOnly) {
      return
    }
    if (this.state.userHasRated) {
      var number
      if (this.state.userRate === -1) {
        number = 0
      } else {
        number = -1
      }
      this.handleRateModify(number, this.state.userRateId)
    } else {
      this.handleRateCreate(-1)
    }
  },
  getInitialState: function () {
    return {
      positiveRates: this.props.positiveRates,
      negativeRates: this.props.negativeRates,
      userHasRated: this.props.userRate !== null,
      userRate: this.props.userRate,
      userRateId: this.props.userRateId
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
            h('a.icon.fa-chevron-up.comment-rate-up' + (this.state.userRate === 1 ? '.is-selected' : ''), {
              href: '#',
              onClick: this.rateUp,
              'aria-hidden': true
            }, this.state.positiveRates
          )
          ]),
          h('li.entry', [
            h('a.icon.fa-chevron-down.comment-rate-down' + (this.state.userRate === -1 ? '.is-selected' : ''), {
              href: '#',
              onClick: this.rateDown,
              'aria-hidden': true
            }, this.state.negativeRates
            )
          ])
        ])
      )
    }
    if (this.props.style === 'ideas') {
      return (
        h('div.idea-rate', [
          h('a.idea-rate-btn.idea-rate-up' + (this.state.userRate === 1 ? '.is-selected' : ''), {
            href: '#',
            title: 'Vote Up',
            onClick: this.rateUp
          }, [
            h('i.fa.fa-chevron-up', [
              h('span', ' ' + this.state.positiveRates)
            ])
          ]
          ),
          h('a.idea-rate-btn.idea-rate-down' + (this.state.userRate === -1 ? '.is-selected' : ''), {
            href: '#',
            title: 'Vote Down',
            onClick: this.rateDown
          }, [
            h('i.fa.fa-chevron-down', [
              h('span', ' ' + this.state.negativeRates)
            ])
          ])
        ])
      )
    }
  }
})

module.exports.RateBox = RateBox

module.exports.renderRates = function (url, positiveRates, negativeRates, userRate, userRateId, loginUrl, contentType, objectId, authenticatedAs, style, target, isReadOnly) {
  ReactDOM.render(
    h(RateBox, {
      url: url,
      positiveRates: positiveRates,
      negativeRates: negativeRates,
      userRate: userRate,
      userRateId: userRateId,
      loginUrl: loginUrl,
      contentType: contentType,
      objectId: objectId,
      authenticatedAs: authenticatedAs,
      pollInterval: 20000,
      style: style,
      isReadOnly: isReadOnly
    }),
    document.getElementById(target)
  )
}
