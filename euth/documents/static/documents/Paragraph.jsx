const React = require('react')
const django = require('django')
const PropTypes = require('prop-types')

class Paragraph extends React.Component {
  add () {
    this.props.addParagraphBeforeIndex(this.props.index)
  }

  delete () {
    this.props.deleteParagraph(this.props.index)
  }

  up () {
    this.props.moveParagraphUp(this.props.index)
  }

  down () {
    this.props.moveParagraphDown(this.props.index)
  }

  handleNameChange (e) {
    const index = this.props.index
    const text = e.target.value
    this.props.updateParagraphName(index, text)
  }

  ckEditorDestroy (id) {
    const editor = window.CKEDITOR.instances[id]
    editor.destroy()
  }

  ckEditorCreate (id) {
    const editor = window.CKEDITOR.replace(id, this.props.config)
    editor.on('change', function (e) {
      const text = e.editor.getData()
      const index = this.props.index
      this.props.updateParagraphText(index, text)
    }.bind(this))
    editor.setData(this.props.paragraph.text)
  }

  UNSAFE_componentWillUpdate () {
    const id = 'id_paragraphs-' + this.props.id + '-text'
    this.ckEditorDestroy(id)
  }

  componentDidUpdate () {
    const id = 'id_paragraphs-' + this.props.id + '-text'
    this.ckEditorCreate(id)
  }

  componentDidMount () {
    const id = 'id_paragraphs-' + this.props.id + '-text'
    this.ckEditorCreate(id)
  }

  render () {
    const ckEditorToolbarsHeight = 60 // measured on example editor
    return (
      <div>
        <div className="row">
          <div className="col-md-9">
            <button
              className="btn btn-hover-success btn-block"
              onClick={this.add.bind(this)}
              type="button"
            >
              <i className="fa fa-plus" /> {django.gettext('add a new paragraph')}
            </button>
          </div>
        </div>
        <div
          className="section row commenting-paragraph"
          id={'paragraphs' + this.props.id}
        >
          <div className="col-sm-9 paragraph">
            <div className="form-group">
              <label
                htmlFor={'id_paragraphs-' + this.props.id + '-name'}
              >
                {django.gettext('Headline:')}
              </label>
              <input
                className="form-control"
                id={'id_paragraphs-' + this.props.id + '-name'}
                name={'paragraphs-' + this.props.id + '-name'}
                type="text"
                defaultValue={this.props.paragraph.name}
                onChange={this.handleNameChange.bind(this)}
              />
              {this.props.errors && this.props.errors.name
                ? <ul className="errorlist"><li>{this.props.errors.name[0]}</li></ul>
                : null}
              <label
                htmlFor={'id_paragraphs-' + this.props.id + '-text'}
              >
                {django.gettext('Paragraph:')}
              </label>
              <div
                className="django-ckeditor-widget"
                data-field-id={'id_paragraphs-' + this.props.id + '-text'}
                style={{ display: 'inline-block' }}
              >
                <textarea
                  id={'id_paragraphs-' + this.props.id + '-text'}
                  style={{ height: this.props.config.height + ckEditorToolbarsHeight }}
                />
                {this.props.errors && this.props.errors.text
                  ? <ul className="errorlist"><li>{this.props.errors.text[0]}</li></ul>
                  : null /* eslint-disable-line */ }
              </div>
            </div>
          </div>

          <div className="col-sm-3 comment-count">
            <div className="action-bar">
              {this.props.moveParagraphUp /* eslint-disable indent, react/jsx-indent */
                ? <button
                    className="btn btn-hover-primary"
                    onClick={this.up.bind(this)}
                    type="button"
                  >
                    <i className="fa fa-chevron-up" />
                  </button>
                : <button
                    className="btn btn-hover-primary"
                    type="button"
                  >
                    <i className="fa fa-chevron-up" />
                  </button>}
              {this.props.moveParagraphDown
                ? <button
                    className="btn btn-hover-primary"
                    onClick={this.down.bind(this)}
                    type="button"
                  >
                    <i className="fa fa-chevron-down" />
                  </button>
                : <button
                    className="btn btn-hover-primary"
                    disabled="true"
                    type="button"
                  >
                    <i className="fa fa-chevron-down" />
                  </button> /* eslint-enable indent, react/jsx-indent */}
              <button
                className="btn btn-hover-danger"
                onClick={this.delete.bind(this)}
                type="button"
              >
                <i className="fas fa-trash-alt" />
              </button>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

Paragraph.propTypes = {
  index: PropTypes.number.isRequired,
  id: PropTypes.string.isRequired,
  config: PropTypes.object,
  errors: PropTypes.object,
  paragraph: PropTypes.shape({
    name: PropTypes.string,
    text: PropTypes.string
  }),
  weight: PropTypes.number,
  addParagraphBeforeIndex: PropTypes.func.isRequired,
  deleteParagraph: PropTypes.func.isRequired,
  moveParagraphUp: PropTypes.func,
  moveParagraphDown: PropTypes.func,
  updateParagraphName: PropTypes.func.isRequired,
  updateParagraphText: PropTypes.func.isRequired
}

module.exports = Paragraph
