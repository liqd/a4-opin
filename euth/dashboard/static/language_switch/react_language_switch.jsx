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
    e.preventDefault()
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
        <ul className="checkbox-list" ref={this.checkboxListRef} role="tablist">
          {
            this.props.languages.map((languageCode, i) => {
              return (
                <li
                  key={languageCode}
                  role="presentation"
                  className={languageCode === this.state.activeTab ? 'nav-item active' : 'nav-item'}
                >
                  <input
                    type="checkbox"
                    name={languageCode}
                    id={languageCode + '_language-switch'}
                    value={languageCode}
                    checked={this.state.activeLanguages.indexOf(languageCode) !== -1} readOnly
                  />
                  <button
                    href={'#' + languageCode + '_language_panel'}
                    id={languageCode + '_language-switch-tab'}
                    className={'language-switch btn ' + (languageCode === this.state.activeTab ? 'active' : '')}
                    data-bs-toggle="tab"
                    onClick={this.activateTab.bind(this)}
                  >{languageCode}
                  </button>
                </li>
              )
            })
          }
        </ul>
        <div className="dropdown ms-5">
          <button
            className="btn btn-secondary dropdown-toggle"
            type="button"
            data-bs-toggle="dropdown"
            ref={this.toggleButtonRef}
          >
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
                        data-bs-toggle="tab"
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
            <button className="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" ref={this.toggleButtonRef}>
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
                        data-bs-toggle="tab"
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
        <div className="tab-content">
          {this.props.languages.map((languageCode, i) => {
            return (
              <div
                key={languageCode + '-panel'}
                className={'tab-panel language-switch-panel  ' + (languageCode === this.state.activeTab ? 'active' : '')}
                id={languageCode + '_language_panel'}
                role="tabpanel"
                aria-labelledby={languageCode + '_language_panel-tab'}
              >
                <div class="form-group">
                  <label class="form-label" htmlFor={'id_' + languageCode + '__description_why'}>Description why are we part of OPIN</label>
                  <textarea
                    id={'id_' + languageCode + '__description_why'}
                    className="form-control"
                    cols="40"
                    rows="10"
                    placeholder={languageCode + ' content'}
                  />
                </div>
              </div>
            )
          })}
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
