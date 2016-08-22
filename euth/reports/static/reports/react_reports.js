var $ = require('jquery')
var React = require('react')
var h = require('react-hyperscript')
var cookie = require('js-cookie')
var django = require('django')

$(function () {
  $.ajaxSetup({
    headers: { 'X-CSRFToken': cookie.get('csrftoken') }
  })
})

var ReportModal = React.createClass({
  getInitialState: function () {
    return {report: ''}
  },
  handleTextChange: function (e) {
    this.setState({report: e.target.value})
  },
  submitReport: function (e) {
    $.ajax({
      url: '/api/reports/',
      dataType: 'json',
      type: 'POST',
      data: {
        description: this.state.report,
        content_type: this.props.contentType,
        object_pk: this.props.objectId
      },
      success: function (report) {
        this.setState({
          report: ''
        })
      }.bind(this),
      error: function (xhr, status, err) {
        console.error(this.props.url, status, err.toString())
      }.bind(this)
    })
  },
  render: function () {
    return h('div.modal.fade#' + this.props.name, { tabindex: '-1', role: 'dialog', 'aria-labelledby': 'myModalLabel' }, [
      h('div.modal-dialog', { role: 'document' }, [
        h('div.modal-content', [
          h('div.modal-header', [
            h('button.close', {
              type: 'button',
              'data-dismiss': 'modal',
              'aria-label': this.props.abort
            }, [
              h('i.fa.fa-times', {
                'aria-hidden': true
              })
            ])
          ]),
          h('div.modal-body', [
            h('h3.modal-title', this.props.title),
            h('div.form-group', [
              h('textarea.form-control', {
                type: 'text',
                placeholder: django.gettext('Your report here'),
                rows: 5,
                required: 'required',
                value: this.state.report,
                onChange: this.handleTextChange
              })
            ])
          ]),
          h('div.modal-footer', [
            h('div.row', [
              h('button.btn.btn-' + (this.props.btnStyle || 'primary'),
                {
                  type: 'button',
                  'onClick': this.submitReport
                },
                django.gettext('Send Report'))
            ]),
            h('div.row', [
              h('button.btn', {
                type: 'button',
                'data-dismiss': 'modal'
              }, django.gettext('Abort'))
            ])
          ])
        ])
      ])
    ])
  }

})

module.exports.ReportModal = ReportModal
