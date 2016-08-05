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

  loadRatesFromServer: function () {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      data: {
        object_pk: this.props.objectId,
        content_type: this.props.contentType
      },
      success: function (rates) {
        this.updateRateList(rates)
      }.bind(this),
      error: function (xhr, status, err) {
        console.error(this.props.url, status, err.toString())
      }.bind(this)
    })
  },
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
        this.state.rates.push(data)
        this.updateRateList(this.state.rates)
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
        this.updateUserRate(data)
        this.updateRateList(this.state.rates)
      }.bind(this),
      error: function (xhr, status, err) {
        console.error(status, err.toString())
      }
    })
  },
  updateRateList: function (rates) {
    var positiveRates = 0
    var negativeRates = 0
    var userHasRated = false
    var userRate = 0
    var userRateId = -1
    var userRateIndex = -1
    var username = this.props.username
    $.each(rates, function (index, value) {
      if (value.user_name === username) {
        userHasRated = true
        userRate = value.value
        userRateId = value.id
        userRateIndex = index
      }
      if (value.value === 1) positiveRates++
      if (value.value === -1) negativeRates++
    })
    this.setState({
      positiveRates: positiveRates,
      negativeRates: negativeRates,
      rates: rates,
      userHasRated: userHasRated,
      userRate: userRate,
      userRateId: userRateId,
      userRateIndex: userRateIndex
    })
  },
  updateUserRate: function (data) {
    this.state.rates[this.state.userRateIndex] = data
  },
  rateUp: function (e) {
    e.preventDefault()
    if (!this.props.isAuthenticated) {
      window.location.replace('/' + this.props.loginUrl)
    }
    if (this.state.userHasRated) {
      var number
      if (this.state.userRate === 1) number = 0
      else if (this.state.userRate === 0) number = 1
      else number = 1
      this.handleRateModify(number, this.state.userRateId)
    } else this.handleRateCreate(1)
  },
  rateDown: function (e) {
    e.preventDefault()
    if (!this.props.isAuthenticated) {
      window.location.replace('/' + this.props.loginUrl)
    }
    if (this.state.userHasRated) {
      var number
      if (this.state.userRate === -1) number = 0
      else if (this.state.userRate === 0) number = -1
      else number = -1
      this.handleRateModify(number, this.state.userRateId)
    } else this.handleRateCreate(-1)
  },
  getRateUpstyle: function () {
    if (this.state.userRate === 1) return 'a.idea-rate-btn.idea-rate-up.is-selected'
    else return 'a.idea-rate-btn.idea-rate-up'
  },
  getRateDownstyle: function () {
    if (this.state.userRate === -1) return 'a.idea-rate-btn.idea-rate-down.is-selected'
    else return 'a.idea-rate-btn.idea-rate-down'
  },
  getInitialState: function () {
    return {
      positiveRates: 0,
      negativeRates: 0,
      userHasRated: false,
      userRate: 0
    }
  },
  componentDidMount: function () {
    this.loadRatesFromServer()
    setInterval(this.loadRatesFromServer, this.props.pollInterval)
  },
  render: function () {
    if (this.props.style === 'comments') {
      return (
        h('ul.nav.navbar-nav', [
          h('li.entry', [
            h('a.icon.fa-chevron-up.comment-rate-up', {
              href: '#',
              onClick: this.rateUp,
              'aria-hidden': true
            }, this.state.positiveRates
          )
          ]),
          h('li.entry', [
            h('a.icon.fa-chevron-down.comment-rate-down', {
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
          h(this.getRateUpstyle(), {
            href: '#',
            title: 'Vote Up',
            onClick: this.rateUp
          }, [
            h('i.fa.fa-chevron-up', [
              h('span', ' ' + this.state.positiveRates)
            ])
          ]
          ),
          h(this.getRateDownstyle(), {
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

module.exports.renderRates = function (url, loginUrl, contentType, objectId, isAuthenticated, username, style, target) {
  ReactDOM.render(
    h(RateBox, {
      url: url,
      loginUrl: loginUrl,
      contentType: contentType,
      objectId: objectId,
      isAuthenticated: isAuthenticated,
      pollInterval: 20000,
      username: username,
      style: style
    }),
    document.getElementById(target)
  )
}
