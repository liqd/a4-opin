var React = require('react')
var ReactDOM = require('react-dom')
var $ = require('jquery')

var LanguageSwitch = React.createClass({
  switchLanguage: function (e) {
    var languageCode = e.target.textContent
    var index = this.state.activeLanguages.indexOf(languageCode)
    var newActiveLanguages = this.state.activeLanguages.concat([])
    if (index === -1) {
      // adding language
      newActiveLanguages.push(languageCode)
    } else {
      newActiveLanguages.splice(index, 1)
    }

    this.setState({
      activeLanguages: newActiveLanguages
    }, function () {
      var $checkbox = $('#' + languageCode + '_language-switch')
      // language was active
      if (!$checkbox.is(':checked')) {
        $(this.refs.checkboxList).find(':checked').first().next('a').tab('show')
      } else {
        $checkbox.next('a').tab('show')
      }
    })
  },
  getInitialState: function () {
    return {
      activeLanguages: this.props.activeLanguages
    }
  },
  componentDidMount: function () {
    $(this.refs.toggleButton).dropdown()
    $(this.refs.checkboxList).find('.a').tab()
  },
  render: function () {
    return (
      <div>
        <ul className="checkbox-list" ref="checkboxList">
          {
            this.props.languages.map((languageCode, i) => {
              return (
                <li key={languageCode} className={i === 0 ? 'active' : ''}>
                  <input type="checkbox" name={languageCode} id={languageCode + '_language-switch'} value={languageCode}
                    checked={this.state.activeLanguages.indexOf(languageCode) !== -1} readOnly />
                  <a href={'#' + languageCode + '_language_panel'} className="language-switch btn"
                    data-toggle="tab">{languageCode}</a>
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
                    <button type="button" onClick={this.switchLanguage}>{languageCode}</button>
                  </li>
                )
              })
            }
          </ul>
        </div>
      </div>
    )
  }
})

LanguageSwitch.propTypes = {
  activeLanguages: React.PropTypes.array
}

module.exports.renderLanguageSwitch = function (el) {
  let languages = el.getAttribute('data-languages').split(' ')
  let activeLanguages = el.getAttribute('data-active-languages').split(' ')

  ReactDOM.render(
    <LanguageSwitch languages={languages} activeLanguages={activeLanguages} />,
    el
  )
}
