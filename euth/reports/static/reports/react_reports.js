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
    return {
      report: '',
      showSuccessMessage: false,
      showErrorMessage: false,
      showReportForm: true
    }
  },
  handleTextChange: function (e) {
    this.setState({report: e.target.value})
  },
  resetModal: function () {
    if (!$('#' + this.props.name).is(':visible')) {
      this.setState({
        report: '',
        showSuccessMessage: false,
        showErrorMessage: false,
        showReportForm: true,
        errors: null
      })
    } else {
      setTimeout(this.resetModal, 500)
    }
  },
  closeModal: function () {
    $('#' + this.props.name).modal('hide')
    this.resetModal()
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
          report: '',
          showSuccessMessage: true,
          showReportForm: false,
          showErrorMessage: false
        })
      }.bind(this),
      error: function (xhr, status, err) {
        this.setState({
          report: '',
          errors: JSON.parse(xhr.responseText)
        })
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
              'onClick': this.closeModal,
              'aria-label': this.props.abort
            }, [
              h('i.fa.fa-times', {
                'aria-hidden': true
              })
            ])
          ]),
          this.state.showSuccessMessage ? h('div.modal-body', [
            h('h3.modal-title', this.props.title),
            h('div.alert.alert-success', django.gettext('Your report has been sent'))
          ]) : null,
          this.state.showReportForm ? h('div.modal-body', [
            h('h3.modal-title', this.props.title),
            h('div.form-group', [
              h('textarea.form-control', {
                type: 'text',
                placeholder: django.gettext('Your report here'),
                rows: 5,
                value: this.state.report,
                onChange: this.handleTextChange
              })
            ]),
            this.state.errors ? h('span.help-block', this.state.errors.description) : null
          ]) : null,
          this.state.showReportForm ? h('div.modal-footer', [
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
                'onClick': this.closeModal
              }, django.gettext('Abort'))
            ])
          ]) : null
        ])
      ])
    ])
  }
})

module.exports.ReportModal = ReportModal
