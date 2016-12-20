var React = require('react')
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
  },
  componentDidMount: function () {
    var id = 'id_paragraphs-' + this.props.id + '-text'
    this.ckEditorCreate(id)
  },
  render: function () {
    var ckEditorToolbarsHeight = 60  // measured on example editor
    return (
      <div>
        <div className="row">
          <div className="col-md-9">
            <button
              className="btn btn-hover-success btn-block"
              onClick={this.add}
              type="button">
              <i className="fa fa-plus" />
            </button>
          </div>
        </div>
        <div
          className="section row commenting-paragraph"
          id={'paragraphs' + this.props.id}>
          <div className="col-sm-9 paragraph">
            <div className="form-group">
              <label
                htmlFor={'id_paragraphs-' + this.props.id + '-name'}>
                {django.gettext('Headline:')}
              </label>
              <input
                className="form-control"
                id={'id_paragraphs-' + this.props.id + '-name'}
                name={'paragraphs-' + this.props.id + '-name'}
                type="text"
                defaultValue={this.props.paragraph.name}
                onChange={this.handleNameChange} />
              {this.props.errors && this.props.errors.name ? <ul className="errorlist">
                <li>{this.props.errors.name[0]}</li>
              </ul> : null}
              <label
                htmlFor={'id_paragraphs-' + this.props.id + '-text'}>
                {django.gettext('Paragraph:')}
              </label>
              <div
                className="django-ckeditor-widget"
                data-field-id={'id_paragraphs-' + this.props.id + '-text'}
                style={{display: 'inline-block'}}>
                <textarea
                  id={'id_paragraphs-' + this.props.id + '-text'}
                  style={{height: this.props.config.height + ckEditorToolbarsHeight}} />
                { this.props.errors && this.props.errors.text ? <ul className="errorlist">
                  <li>{this.props.errors.text[0]}</li>
                </ul> : null }
              </div>
            </div>
          </div>
          <div className="col-sm-3 comment-count">
            <div className="action-bar">
              { this.props.moveParagraphUp
              ? <button
                className="btn btn-hover-primary"
                onClick={this.up}
                type="button">
                <i className="fa fa-chevron-up" />
              </button>
              : <button
                className="btn btn-hover-primary"
                disabled="true"
                type="button">
                <i className="fa fa-chevron-up" />
              </button> }
              { this.props.moveParagraphDown
              ? <button
                className="btn btn-hover-primary"
                onClick={this.down}
                type="button">
                <i className="fa fa-chevron-down" />
              </button>
              : <button
                className="btn btn-hover-primary"
                disabled="true"
                type="button">
                <i className="fa fa-chevron-down" />
              </button> }
              <button
                className="btn btn-hover-danger"
                onClick={this.delete}
                type="button">
                <i className="fa fa-trash" />
              </button>
            </div>
          </div>
        </div>
      </div>
    )
  }
})

module.exports = Paragraph
