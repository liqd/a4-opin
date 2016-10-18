var React = require('react')
var h = require('react-hyperscript')

module.exports.Modal = React.createClass({
  'render': function () {
    return h('div.modal.fade#' + this.props.name, { tabindex: '-1', role: 'dialog', 'aria-labelledby': 'myModalLabel' }, [
      h('div.modal-dialog.modal-lg', { role: 'document' }, [
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
            h('h3.modal-title', this.props.question)
          ]),
          h('div.modal-footer', [
            h('div.row', [
              h('button.submit-button',
                {
                  type: 'button',
                  'data-dismiss': 'modal',
                  onClick: this.props.handler
                },
                this.props.action)
            ]),
            h('div.row', [
              h('button.cancel-button', {
                type: 'button',
                'data-dismiss': 'modal'
              }, this.props.abort)
            ])
          ])
        ])
      ])
    ])
  }
})
