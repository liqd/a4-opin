var api = require('../../../contrib/static/js/api')

var $ = require('jquery')
var React = require('react')
var h = require('react-hyperscript')
var django = require('django')

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
    api.report.submit({
      description: this.state.report,
      content_type: this.props.contentType,
      object_pk: this.props.objectId
    })
      .done(function () {
        this.setState({
          report: '',
          showSuccessMessage: true,
          showReportForm: false,
          showErrorMessage: false
        })
      }.bind(this))
  },
  render: function () {
    return h('div.modal.fade#' + this.props.name, { tabindex: '-1', role: 'dialog', 'aria-labelledby': 'myModalLabel' }, [
      h('div.modal-dialog.modal-lg', { role: 'document' }, [
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
          this.state.showSuccessMessage ? h('div.modal-body.success', [
            h('h3.modal-title', [
              h('i.fa.fa-check'),
              'Thank you! We are taking care of it.'
            ])
          ]) : null,
          this.state.showReportForm ? h('div.modal-body', [
            h('h3.modal-title', this.props.title),
            h('div.form-group', [
              h('textarea.form-control.report-message', {
                type: 'text',
                placeholder: django.gettext('Your message here'),
                rows: 5,
                value: this.state.report,
                onChange: this.handleTextChange
              })
            ]),
            this.state.errors ? h('span.help-block', this.state.errors.description) : null
          ]) : null,
          this.state.showReportForm ? h('div.modal-footer', [
            h('div.row', [
              h('button.submit-button',
                {
                  type: 'button',
                  'onClick': this.submitReport
                },
                django.gettext('Send Report'))
            ]),
            h('div.row', [
              h('button.cancel-button', {
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
