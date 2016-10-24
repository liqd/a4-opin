var React = require('react')
var h = require('react-hyperscript')
var django = require('django')

var Paragraph = React.createClass({
  getInitialState: function () {
    return {
      name: this.props.paragraph.name,
      text: this.props.paragraph.text,
      weight: this.props.index
    }
  },
  add: function () {
    this.props.addParagraphBeforeIndex(this.props.index)
  },
  delete: function () {
    this.props.deleteParagraph(this.props.index)
  },
  up: function () {
    this.props.moveParagraphUp(this.props.index, this)
  },
  down: function () {
    this.props.moveParagraphDown(this.props.index, this)
  },
  handleNameChange: function (e) {
    var index = this.props.index
    var text = e.target.value
    this.props.updateParagraphName(index, text)
  },
  componentDidMount: function () {
    var id = 'id_paragraphs-' + this.props.index + '-text'
    var editor = window.CKEDITOR.replace(id, this.props.config)
    editor.on('change', function (e) {
      var text = e.editor.getData()
      var index = this.props.index
      this.props.updateParagraphText(index, text)
    }.bind(this))
    editor.setData(this.state.text)
    this.props.updateParagraphWeight(this.state.weight)
  },
  render: function () {
    return (
      h('div', [
        h('div.row', [
          h('div.col-md-2.col-md-offset-4', [
            h('a', { onClick: this.add }, [
              h('i.fa.fa-plus')
            ])
          ])
        ]),
        h('section.row.commenting-paragraph', {
          id: 'paragraphs' + this.props.index
        }, [
          h('div.col-sm-9.paragraph', [
            h('div.form-group', [
              h('label', {
                htmlFor: 'id_paragraphs-' + this.props.index + '-name'
              }, django.gettext('Headline:')),
              h('input.form-control', {
                id: 'id_paragraphs-' + this.props.index + '-name',
                name: 'paragraphs-' + this.props.index + '-name',
                type: 'text',
                defaultValue: this.state.name,
                onChange: this.handleNameChange
              }),
              h('label', {
                htmlFor: 'id_paragraphs-' + this.props.index + '-text'
              }, django.gettext('Paragraph:')),
              h('div.django-ckeditor-widget', {
                'data-field-id': 'id_paragraphs-' + this.props.index + '-text',
                'style': {display: 'inline-block'}
              }, [
                h('textarea', {
                  id: 'id_paragraphs-' + this.props.index + '-text'
                }),
                this.props.errors && this.props.errors.text ? h('ul.errorlist', [
                  h('li', this.props.errors.text[0])
                ]) : null
              ])
            ])
          ]),
          h('div.col-sm-3.comment-count', [
            h('div.action-bar', [
              h('nav.navbar.navbar-default.navbar-static', [
                h('ul.nav.navbar-nav', [
                  h('li.entry', [
                    h('a', { onClick: this.up }, [
                      h('i.fa.fa-chevron-up')
                    ])
                  ]),
                  h('li.entry', [
                    h('a', { onClick: this.down }, [
                      h('i.fa.fa-chevron-down')
                    ])
                  ]),
                  h('li.entry', [
                    h('a', { onClick: this.delete }, [
                      h('i.fa.fa-trash')
                    ])
                  ])
                ])
              ])
            ])
          ])
        ])
      ])
    )
  }
})

module.exports = Paragraph
