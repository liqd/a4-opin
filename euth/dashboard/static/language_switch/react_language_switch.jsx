const PropTypes = require('prop-types')
const React = require('react')
const ReactDOM = require('react-dom')

class LanguageSwitch extends React.Component {
  constructor (props) {
    super(props)
    this.checkboxListRef = React.createRef()
    this.toggleButtonRef = React.createRef()

    this.state = {
      activeLanguages: this.props.activeLanguages,
      activeTab: this.getInitialActiveTab()
    }
  }

  getInitialActiveTab () {
    if (this.props.activeLanguages.length > 0) {
      return this.props.activeLanguages[0]
    } else {
      return 'en'
    }
  }

  getNewActiveTab (removedLanguage) {
    const index = this.state.activeLanguages.indexOf(removedLanguage)
    const newActiveLanguages = this.state.activeLanguages.concat([])
    if (index !== -1) {
      newActiveLanguages.splice(index, 1)
    }
    if (newActiveLanguages.length > 0) {
      return newActiveLanguages[0]
    } else {
      return ''
    }
  }

  activateTab (e) {
    const languageCode = e.target.textContent
    this.setState({ activeTab: languageCode })
  }

  addLanguage (e) {
    const languageCode = e.target.textContent
    const index = this.state.activeLanguages.indexOf(languageCode)
    const newActiveLanguages = this.state.activeLanguages.concat([])
    if (index === -1) {
      // adding language
      newActiveLanguages.push(languageCode)
    }

    this.setState({
      activeLanguages: newActiveLanguages,
      activeTab: languageCode
    })
  }

  removeLanguage (e) {
    const languageCode = e.target.textContent
    const index = this.state.activeLanguages.indexOf(languageCode)
    const newActiveLanguages = this.state.activeLanguages.concat([])
    if (index !== -1) {
      // removing language
      newActiveLanguages.splice(index, 1)
    }
    this.setState({
      activeLanguages: newActiveLanguages
    })
    if (this.state.activeTab === languageCode) {
      this.setState({
        activeTab: this.getNewActiveTab(languageCode)
      })
    }
  }

  render () {
    return (
      <div>
        <ul className="checkbox-list" ref={this.checkboxListRef}>
          {
            this.props.languages.map((languageCode, i) => {
              return (
                <li key={languageCode} className={languageCode === this.state.activeTab ? 'active' : ''}>
                  <input
                    type="checkbox" name={languageCode} id={languageCode + '_language-switch'} value={languageCode}
                    checked={this.state.activeLanguages.indexOf(languageCode) !== -1} readOnly
                  />
                  <button
                    href={'#' + languageCode + '_language_panel'} className={'language-switch btn ' + (languageCode === this.state.activeTab ? 'active' : '')}
                    data-toggle="tab" onClick={this.activateTab.bind(this)}
                  >{languageCode}
                  </button>
                </li>
              )
            })
          }
        </ul>
        <div className="dropdown ml-5">
          <button className="btn btn-secondary dropdown-toggle" type="button" data-toggle="dropdown" ref={this.toggleButtonRef}>
            <i className="fa fa-plus" />
          </button>
          <div className="dropdown-menu">
            {
              this.props.languages.map((languageCode, i) => {
                return (
                  <span key={languageCode}>
                    {this.state.activeLanguages.indexOf(languageCode) === -1 &&
                      <button
                        href={'#' + languageCode + '_language_panel'}
                        className="dropdown-item"
                        data-toggle="tab"
                        onClick={this.addLanguage.bind(this)}
                        key={languageCode}
                      >{languageCode}
                      </button>}
                  </span>

                )
              })
            }
          </div>
        </div>

        {this.state.activeLanguages.length > 1 &&
          <div className="dropdown">
            <button className="btn btn-secondary dropdown-toggle" type="button" data-toggle="dropdown" ref={this.toggleButtonRef}>
              <i className="fa fa-minus" />
            </button>
            <div className="dropdown-menu">
              {
                this.state.activeLanguages.map(languageCode => {
                  return (
                    <span key={languageCode}>
                      <button
                        className="dropdown-item"
                        href={languageCode === this.state.activeTab ? '#' + this.getNewActiveTab(languageCode) + '_language_panel' : ''}
                        data-toggle="tab"
                        onClick={this.removeLanguage.bind(this)}
                        key={languageCode}
                      >{languageCode}
                      </button>
                    </span>
                  )
                })
              }
            </div>
          </div>}
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
