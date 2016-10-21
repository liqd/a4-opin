var api = require('../../../contrib/static/js/api')
var Paragraph = require('./Paragraph.js')
var React = require('react')
var ReactDOM = require('react-dom')
var h = require('react-hyperscript')
var update = require('react-addons-update')
var django = require('django')

var ParagraphBox = React.createClass({
  getInitialState: function () {
    return {
      id: this.props.id,
      name: this.props.name,
      paragraphs: this.props.paragraphs,
      nameErrors: [],
      paragraphsErrors: []
    }
  },
  handleDocumentNameChange: function (e) {
    this.setState({
      name: e.target.value
    })
  },
  getNewParagraph: function (name, text) {
    var newParagraph = {}
    newParagraph['name'] = name
    newParagraph['text'] = text
    return newParagraph
  },
  deleteParagraph: function (index) {
    var newArray = update(this.state.paragraphs, {$splice: [[index, 1]]})
    this.setState({
      paragraphs: newArray
    })
  },
  moveParagraphUp: function (index, paragraph) {
    var newParagraph = this.getNewParagraph(paragraph.state.name, paragraph.state.text)
    var newArray = update(this.state.paragraphs, {$splice: [[index, 1]]})
    newArray.splice(index - 1, 0, newParagraph)
    this.setState({
      paragraphs: newArray
    })
  },
  moveParagraphDown: function (index, paragraph) {
    var newParagraph = this.getNewParagraph(paragraph.state.name, paragraph.state.text)
    var newArray = update(this.state.paragraphs, {$splice: [[index, 1]]})
    newArray.splice(index + 1, 0, newParagraph)
    this.setState({
      paragraphs: newArray
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
    this.state.paragraphs[index].name = name
  },
  updateParagraphText: function (index, text) {
    this.state.paragraphs[index].text = text
  },
  updateParagraphWeight: function (weight) {
    this.state.paragraphs[weight].weight = weight
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
  counter: 1,
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
          this.state.paragraphs.map(function (paragraph, index) {
            var count = this.counter++
            return (
              h(Paragraph, {
                key: count,
                visibleKey: count,
                index: index,
                pk: paragraph.pk,
                paragraph: paragraph,
                errors: this.getErrors(index),
                config: this.props.config,
                deleteParagraph: this.deleteParagraph,
                moveParagraphUp: this.moveParagraphUp,
                moveParagraphDown: this.moveParagraphDown,
                addParagraphBeforeIndex: this.addParagraphBeforeIndex,
                updateParagraphName: this.updateParagraphName,
                updateParagraphText: this.updateParagraphText,
                updateParagraphWeight: this.updateParagraphWeight
              }
              )
            )
          }.bind(this)),
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
