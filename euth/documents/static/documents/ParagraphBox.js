var api = require('../../../contrib/static/js/api')
var Paragraph = require('./Paragraph.js')
var React = require('react')
var ReactDOM = require('react-dom')
var h = require('react-hyperscript')
var update = require('react-addons-update')
var django = require('django')
var FlipMove = require('react-flip-move')

var ParagraphBox = React.createClass({
  getInitialState: function () {
    return {
      id: this.props.id,
      name: this.props.name,
      paragraphs: this.props.paragraphs,
      nameErrors: [],
      paragraphsErrors: [],
      maxParagraphKey: 0
    }
  },
  handleDocumentNameChange: function (e) {
    this.setState({
      name: e.target.value
    })
  },
  getNextParagraphKey: function () {
    /** Get an artifical key for non-commited paragraphs.
     *
     *  Prefix to prevent collisions with real database keys;
     */
    var paragraphKey = 'local_' + (this.state.maxParagraphKey + 1)
    this.setState({maxParagraphKey: this.state.maxParagraphKey + 1})
    return paragraphKey
  },
  getNewParagraph: function (name, text) {
    var newParagraph = {}
    newParagraph['name'] = name
    newParagraph['text'] = text
    newParagraph['paragraph_key'] = this.getNextParagraphKey()
    return newParagraph
  },
  deleteParagraph: function (index) {
    var newArray = update(this.state.paragraphs, {$splice: [[index, 1]]})
    this.setState({
      paragraphs: newArray
    })
  },
  moveParagraphUp: function (index) {
    var paragraph = this.state.paragraphs[index]
    var paragraphs = update(this.state.paragraphs, {
      $splice: [[index, 1], [index - 1, 0, paragraph]]
    })
    this.setState({
      paragraphs: paragraphs
    })
  },
  moveParagraphDown: function (index) {
    var paragraph = this.state.paragraphs[index]
    var paragraphs = update(this.state.paragraphs, {
      $splice: [[index, 1], [index + 1, 0, paragraph]]
    })
    this.setState({
      paragraphs: paragraphs
    })
  },
  addParagraphBeforeIndex: function (index) {
    var newParagraph = this.getNewParagraph('', '')
    var newArray = update(this.state.paragraphs, {$splice: [[index, 0, newParagraph]]})
    this.setState({
      paragraphs: newArray
    })
  },
  appendParagraph: function () {
    var newParagraph = this.getNewParagraph('', '')
    var newArray = update(this.state.paragraphs, {$push: [newParagraph]})
    this.setState({
      paragraphs: newArray
    })
  },
  updateParagraphName: function (index, name) {
    // deliberatly not call setState, because otherwise jkEditor reload/flicker
    this.state.paragraphs[index].name = name
  },
  updateParagraphText: function (index, text) {
    // deliberatly not call setState, because otherwise jkEditor reload/flicker
    this.state.paragraphs[index].text = text
  },
  submitDocument: function (e) {
    if (e) {
      e.preventDefault()
    }
    if (typeof this.state.id !== 'undefined') {
      this.updateDocument(this.state.id)
    } else {
      this.createDocument()
    }
  },
  updateDocument: function (id) {
    var submitData = {}
    submitData['name'] = this.state.name
    submitData['module'] = this.props.module
    this.state.paragraphs.forEach(function (val, index) { val.weigth = index })
    submitData['paragraphs'] = this.state.paragraphs

    api.document.change(JSON.stringify(submitData), id)
      .done(function (data) {
        this.setState({
          name: data.name,
          paragraphs: data.paragraphs
        })
      }.bind(this))
      .fail(function (xhr, status, err) {
        this.setState({
          nameErrors: xhr.responseJSON.name,
          paragraphsErrors: xhr.responseJSON.paragraphs
        })
      }.bind(this))
  },
  createDocument: function () {
    var submitData = {}
    submitData['name'] = this.state.name
    submitData['module'] = this.props.module
    this.state.paragraphs.forEach(function (val, index) { val.weigth = index })
    submitData['paragraphs'] = this.state.paragraphs

    api.document.add(JSON.stringify(submitData))
      .done(function (data) {
        this.setState({
          id: data.id,
          name: data.name,
          paragraphs: data.paragraphs
        })
      }.bind(this))
      .fail(function (xhr, status, err) {
        this.setState({
          nameErrors: xhr.responseJSON.name,
          paragraphsErrors: xhr.responseJSON.paragraphs
        })
      }.bind(this))
  },
  shouldComponentUpdate: function (nextProps, nextState) {
    return !(nextState.name !== this.state.name)
  },
  getErrors: function (index) {
    return this.state.paragraphsErrors[index]
  },
  render: function () {
    return (
      h('div.general-form', [
        h('form', {onSubmit: this.submitDocument}, [
          h('div.row', [
            h('div.col-sm-9', [
              h('div.form-group', [
                h('label', django.gettext('Title:')),
                h('input.form-control', {
                  type: 'text',
                  defaultValue: this.state.name,
                  onChange: this.handleDocumentNameChange
                }),
                this.state.nameErrors && this.state.nameErrors.length > 0 ? h('ul.errorlist', [
                  h('li', this.state.nameErrors[0])
                ]) : null
              ])
            ])
          ]),
          h(FlipMove, {easing: 'cubic-bezier(0.25, 0.5, 0.75, 1)'},
            this.state.paragraphs.map(function (paragraph, index) {
              return h(Paragraph, {
                key: paragraph.paragraph_key || paragraph.id,
                id: paragraph.paragraph_key || paragraph.id,
                index: index,
                paragraph: paragraph,
                errors: this.getErrors(index),
                config: this.props.config,
                deleteParagraph: this.deleteParagraph,
                moveParagraphUp: index !== 0 ? this.moveParagraphUp : null,
                moveParagraphDown: index < this.state.paragraphs.length - 1
                  ? this.moveParagraphDown : null,
                addParagraphBeforeIndex: this.addParagraphBeforeIndex,
                updateParagraphName: this.updateParagraphName,
                updateParagraphText: this.updateParagraphText
              })
            }.bind(this))),
          h('div.row', [
            h('div.col-md-9', [
              h('a.btn.btn-default.btn-block', {
                onClick: this.appendParagraph
              }, [
                h('i.fa.fa-plus')
              ])
            ])
          ]),
          h('button.submit-button', {
            type: 'submit'
          }, 'save')
        ])
      ])
    )
  }
})

module.exports.renderParagraphs = function (doc, module, config) {
  ReactDOM.render(
    h(ParagraphBox, {
      name: doc.name,
      id: doc.id,
      module: module,
      paragraphs: doc.paragraphs,
      config: config
    }),
    document.getElementById('document-form'))
}
