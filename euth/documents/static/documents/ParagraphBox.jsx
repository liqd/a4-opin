const api = require('adhocracy4').api
const Paragraph = require('./Paragraph.jsx')
const PropTypes = require('prop-types')
const React = require('react')
const ReactDOM = require('react-dom')
const update = require('immutability-helper')
const django = require('django')
const FlipMove = require('react-flip-move').default

class ParagraphBox extends React.Component {
  constructor (props) {
    super(props)

    this.state = {
      id: this.props.id,
      name: this.props.name,
      paragraphs: this.props.paragraphs,
      nameErrors: [],
      paragraphsErrors: [],
      maxParagraphKey: 0,
      successMessage: ''
    }
  }

  handleDocumentNameChange (e) {
    this.setState({
      name: e.target.value
    })
  }

  getNextParagraphKey () {
    /** Get an artifical key for non-commited paragraphs.
     *
     *  Prefix to prevent collisions with real database keys;
     */
    const paragraphKey = 'local_' + (this.state.maxParagraphKey + 1)
    this.setState({ maxParagraphKey: this.state.maxParagraphKey + 1 })
    return paragraphKey
  }

  getNewParagraph (name, text) {
    const newParagraph = {}
    newParagraph.name = name
    newParagraph.text = text
    newParagraph.paragraph_key = this.getNextParagraphKey()
    return newParagraph
  }

  deleteParagraph (index) {
    const newArray = update(this.state.paragraphs, { $splice: [[index, 1]] })
    this.setState({
      paragraphs: newArray
    })
  }

  moveParagraphUp (index) {
    const paragraph = this.state.paragraphs[index]
    const paragraphs = update(this.state.paragraphs, {
      $splice: [[index, 1], [index - 1, 0, paragraph]]
    })
    this.setState({
      paragraphs: paragraphs
    })
  }

  moveParagraphDown (index) {
    const paragraph = this.state.paragraphs[index]
    const paragraphs = update(this.state.paragraphs, {
      $splice: [[index, 1], [index + 1, 0, paragraph]]
    })
    this.setState({
      paragraphs: paragraphs
    })
  }

  addParagraphBeforeIndex (index) {
    const newParagraph = this.getNewParagraph('', '')
    const newArray = update(this.state.paragraphs, { $splice: [[index, 0, newParagraph]] })
    this.setState({
      paragraphs: newArray
    })
  }

  appendParagraph () {
    const newParagraph = this.getNewParagraph('', '')
    const newArray = update(this.state.paragraphs, { $push: [newParagraph] })
    this.setState({
      paragraphs: newArray
    })
  }

  updateParagraphName (index, name) {
    // deliberatly not call setState, because otherwise jkEditor reload/flicker
    this.state.paragraphs[index].name = name /* eslint-disable-line */
  }

  updateParagraphText (index, text) {
    // deliberatly not call setState, because otherwise jkEditor reload/flicker
    this.state.paragraphs[index].text = text /* eslint-disable-line */
  }

  submitDocument (e) {
    if (e) {
      e.preventDefault()
    }
    if (typeof this.state.id !== 'undefined') {
      this.updateDocument(this.state.id)
    } else {
      this.createDocument()
    }
  }

  updateDocument (id) {
    const submitData = {
      urlReplaces: { moduleId: this.props.module }
    }
    submitData.name = this.state.name
    this.state.paragraphs.forEach(function (val, index) { val.weight = index })
    submitData.paragraphs = this.state.paragraphs

    api.document.change(submitData, id)
      .done(function (data) {
        this.setState({
          name: data.name,
          paragraphs: data.paragraphs,
          successMessage: django.gettext('Your document has been updated.')
        })
        setTimeout(function () {
          this.setState({
            successMessage: ''
          })
        }.bind(this), 1500)
      }.bind(this))
      .fail(function (xhr, status, err) {
        this.setState({
          nameErrors: xhr.responseJSON.name,
          paragraphsErrors: xhr.responseJSON.paragraphs
        })
      }.bind(this))
  }

  createDocument () {
    const submitData = {
      urlReplaces: { moduleId: this.props.module }
    }
    submitData.name = this.state.name
    this.state.paragraphs.forEach(function (val, index) { val.weight = index })
    submitData.paragraphs = this.state.paragraphs

    api.document.add(submitData)
      .done(function (data) {
        this.setState({
          id: data.id,
          name: data.name,
          paragraphs: data.paragraphs,
          successMessage: django.gettext('Your document has been saved.')
        })
        setTimeout(function () {
          this.setState({
            successMessage: ''
          })
        }.bind(this), 1500)
      }.bind(this))
      .fail(function (xhr, status, err) {
        this.setState({
          nameErrors: xhr.responseJSON.name,
          paragraphsErrors: xhr.responseJSON.paragraphs
        })
      }.bind(this))
  }

  shouldComponentUpdate (nextProps, nextState) {
    return !(nextState.name !== this.state.name)
  }

  getErrors (index) {
    return this.state.paragraphsErrors[index]
  }

  render () {
    return (
      <div className="general-form">
        <form onSubmit={this.submitDocument.bind(this)}>
          <div className="row">
            <div className="col-sm-9">
              <div className="form-group">
                <label>{django.gettext('Title:')}</label>
                <input
                  className="form-control"
                  type="text"
                  defaultValue={this.state.name}
                  onChange={this.handleDocumentNameChange.bind(this)}
                />
              </div>
            </div>
          </div>
          <FlipMove easing="cubic-bezier(0.25, 0.5, 0.75, 1)">
            {
              this.state.paragraphs.map(function (paragraph, index) {
                return (
                  <Paragraph
                    key={paragraph.paragraph_key || paragraph.id}
                    id={paragraph.paragraph_key || (paragraph.id).toString()}
                    index={index}
                    paragraph={paragraph}
                    errors={this.getErrors(index)}
                    config={this.props.config}
                    deleteParagraph={this.deleteParagraph.bind(this)}
                    moveParagraphUp={index !== 0 ? this.moveParagraphUp.bind(this) : null}
                    moveParagraphDown={index < this.state.paragraphs.length - 1 ? this.moveParagraphDown.bind(this) : null}
                    addParagraphBeforeIndex={this.addParagraphBeforeIndex.bind(this)}
                    updateParagraphName={this.updateParagraphName.bind(this)}
                    updateParagraphText={this.updateParagraphText.bind(this)}
                  />
                )
              }.bind(this))
            }
          </FlipMove>
          <div className="row">
            <div className="col-md-9">
              <button
                className="btn btn-hover-success btn-block"
                onClick={this.appendParagraph.bind(this)}
                type="button"
              >
                <i className="fa fa-plus" /> {django.gettext('add a new paragraph')}
              </button>
            </div>
          </div>
          {this.state.successMessage
            ? <div className="row">
              <div className="col-md-9">
                <p className="alert alert-success ">
                  {this.state.successMessage}
                </p>
              </div>
            </div> /* eslint-disable-line */
            : null}
          <button
            id="submit-button"
            className="btn btn-primary"
            type="submit"
          >
            {django.gettext('save')}
          </button>
        </form>
      </div>
    )
  }
}

ParagraphBox.propTypes = {
  id: PropTypes.number,
  name: PropTypes.string,
  module: PropTypes.string.isRequired,
  config: PropTypes.object.isRequired,
  paragraphs: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string,
      text: PropTypes.string,
      weight: PropTypes.number
    })
  )
}

module.exports.renderParagraphs = function (el) {
  const module = el.getAttribute('data-module')
  const doc = JSON.parse(el.getAttribute('data-document'))
  const config = JSON.parse(el.getAttribute('data-config'))

  ReactDOM.render(<ParagraphBox
    name={doc.name}
    id={doc.id}
    module={module}
    paragraphs={doc.paragraphs}
    config={config}
  />, el /* eslint-disable-line */
  )
}
