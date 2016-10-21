var React = require('react')
var h = require('react-hyperscript')
var django = require('django')

var Paragraph = React.createClass({
  add: function () {
    this.props.addParagraphBeforeIndex(this.props.index)
  },
  delete: function () {
    this.props.deleteParagraph(this.props.index)
  },
  up: function () {
    this.props.moveParagraphUp(this.props.index)
  },
  down: function () {
    this.props.moveParagraphDown(this.props.index)
  },
  handleNameChange: function (e) {
    var index = this.props.index
    var text = e.target.value
    this.props.updateParagraphName(index, text)
  },
  ckEditorDestroy: function (id) {
    var editor = window.CKEDITOR.instances[id]
    editor.destroy()
  },
  ckEditorCreate: function (id) {
    var editor = window.CKEDITOR.replace(id, this.props.config)
    editor.on('change', function (e) {
      var text = e.editor.getData()
      var index = this.props.index
      this.props.updateParagraphText(index, text)
    }.bind(this))
    editor.setData(this.props.paragraph.text)
  },
  componentWillUpdate: function () {
    var id = 'id_paragraphs-' + this.props.id + '-text'
    this.ckEditorDestroy(id)
  },
  componentDidUpdate: function () {
    var id = 'id_paragraphs-' + this.props.id + '-text'
    this.ckEditorCreate(id)
    this.props.updateParagraphWeight(this.props.index)
  },
  componentDidMount: function () {
    var id = 'id_paragraphs-' + this.props.id + '-text'
    this.ckEditorCreate(id)
    this.props.updateParagraphWeight(this.props.index)
  },
  render: function () {
    return (
      h('div', [
        h('div.row', [
          h('div.col-md-9', [
            h('a.btn.btn-default.btn-block', {
              onClick: this.add
            }, [
              h('i.fa.fa-plus')
            ])
          ])
        ]),
        h('section.row.commenting-paragraph', {
          id: 'paragraphs' + this.props.id
        }, [
          h('div.col-sm-9.paragraph', [
            h('div.form-group', [
              h('label', {
                htmlFor: 'id_paragraphs-' + this.props.id + '-name'
              }, django.gettext('Headline:')),
              h('input.form-control', {
                id: 'id_paragraphs-' + this.props.id + '-name',
                name: 'paragraphs-' + this.props.id + '-name',
                type: 'text',
                defaultValue: this.props.paragraph.name,
                onChange: this.handleNameChange
              }),
              this.props.errors && this.props.errors.name ? h('ul.errorlist', [
                h('li', this.props.errors.name[0])
              ]) : null,
              h('label', {
                htmlFor: 'id_paragraphs-' + this.props.id + '-text'
              }, django.gettext('Paragraph:')),
              h('div.django-ckeditor-widget', {
                'data-field-id': 'id_paragraphs-' + this.props.id + '-text',
                'style': {display: 'inline-block'}
              }, [
                h('textarea', {
                  id: 'id_paragraphs-' + this.props.id + '-text'
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
                    h('a.tooltipclass', {
                      onClick: this.up}, [
                        h('i.fa.fa-chevron-up.move')
                      ])
                  ]),
                  h('li.entry', [
                    h('a.tooltipclass', {
                      onClick: this.down }, [
                        h('i.fa.fa-chevron-down.move.')
                      ])
                  ]),
                  h('li.entry', [
                    h('a.tooltipclass', {
                      onClick: this.delete }, [
                        h('i.fa.fa-trash.delete')
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
