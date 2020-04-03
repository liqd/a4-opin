var PropTypes = require('prop-types')
var React = require('react')
var ReactDOM = require('react-dom')

class LanguageSwitch extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      activeLanguages: this.props.activeLanguages
    }
  }

  addLanguage (e) {
    var languageCode = e.target.textContent
    var index = this.state.activeLanguages.indexOf(languageCode)
    var newActiveLanguages = this.state.activeLanguages.concat([])
    if (index === -1) {
      // adding language
      newActiveLanguages.push(languageCode)
    }

    this.setState({
      activeLanguages: newActiveLanguages
    })
  }

  removeLanguage (e) {
    var languageCode = e.target.textContent
    var index = this.state.activeLanguages.indexOf(languageCode)
    var newActiveLanguages = this.state.activeLanguages.concat([])
    if (index !== -1) {
      // removing language
      newActiveLanguages.splice(index, 1)
    }

    this.setState({
      activeLanguages: newActiveLanguages
    })
  }

  render () {
    return (
      <div>
        <ul className="checkbox-list" ref="checkboxList">
          {
            this.props.languages.map((languageCode, i) => {
              return (
                <li key={languageCode} className={i === 0 ? 'active' : ''}>
                  <input
                    type="checkbox" name={languageCode} id={languageCode + '_language-switch'} value={languageCode}
                    checked={this.state.activeLanguages.indexOf(languageCode) !== -1} readOnly
                  />
                  <a
                    href={'#' + languageCode + '_language_panel'} className="language-switch btn"
                    data-toggle="tab"
                  >{languageCode}
                  </a>
                </li>
              )
            })
          }
        </ul>
        <div className="dropdown">
          <button className="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown" ref="toggleButton">
            <i className="fa fa-plus" />
          </button>
          <ul className="dropdown-menu">
            {
              this.props.languages.map((languageCode, i) => {
                return (
                  <span key={languageCode}>
                    {this.state.activeLanguages.indexOf(languageCode) === -1 &&
                      <li key={languageCode}>
                        <button type="button" onClick={this.addLanguage.bind(this)}>{languageCode}</button>
                      </li>}
                  </span>
                )
              })
            }
          </ul>
        </div>
        <div className="dropdown">
          <button className="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown" ref="toggleButton">
            <i className="fa fa-minus" />
          </button>
          <ul className="dropdown-menu">
            {
              this.state.activeLanguages.map(languageCode => {
                return (
                  <li key={languageCode}>
                    <button type="button" onClick={this.removeLanguage.bind(this)}>{languageCode}</button>
                  </li>
                )
              })
            }
          </ul>
        </div>
      </div>
    )
  }
}

LanguageSwitch.propTypes = {
  activeLanguages: PropTypes.arrayOf(PropTypes.string)
}

module.exports.renderLanguageSwitch = function (el) {
  const languages = el.getAttribute('data-languages').split(' ')
  const activeLanguages = el.getAttribute('data-active-languages').split(' ')

  ReactDOM.render(
    <LanguageSwitch languages={languages} activeLanguages={activeLanguages} />,
    el
  )
}
