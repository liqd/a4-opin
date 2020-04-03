var PropTypes = require('prop-types')
var React = require('react')
var ReactDOM = require('react-dom')
// var $ = require('jquery')

class LanguageSwitch extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      activeLanguages: this.props.activeLanguages
    }
  }

  switchLanguage (e) {
    var languageCode = e.target.textContent
    var index = this.state.activeLanguages.indexOf(languageCode)
    var newActiveLanguages = this.state.activeLanguages.concat([])
    if (index === -1) {
      // adding language
      newActiveLanguages.push(languageCode)
    } else {
      // removing language
      newActiveLanguages.splice(index, 1)
    }

    this.setState({
      activeLanguages: newActiveLanguages
    })
    //, function () {
    //   var checkbox = $('#' + languageCode + '_language-switch')
    //   // language was active
    //   if (!checkbox.is(':checked')) {
    //     $(this.refs.checkboxList).find(':checked').first().next('a').tab('show')
    //   } else {
    //     checkbox.next('a').tab('show')
    //   }
    // })
  }

  componentDidMount () {
    // $(this.refs.toggleButton).dropdown()
    // $(this.refs.checkboxList).find('.a').tab()
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
              this.props.languages.map(languageCode => {
                return (
                  <li key={languageCode}>
                    <button type="button" onClick={this.switchLanguage.bind(this)}>{languageCode}</button>
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
