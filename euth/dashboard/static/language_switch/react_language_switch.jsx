var React = require('react')
var ReactDOM = require('react-dom')
var $ = require('jquery')

var LanguageSwitch = React.createClass({
  switchLanguage: function (e) {
    var languageCode = e.target.textContent
    var $checkbox = $('#' + languageCode + '_language-switch')
    // language was active
    if ($checkbox.is(':checked')) {
      $(this.refs.checkboxList).find(':checked').first().next('a').tab('show')
    } else {
      $checkbox.next('a').tab('show')
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
                <li className={i === 0 ? '.active' : ''} key={i}>
                  <input type="checkbox" name={languageCode} id={languageCode + '_language-switch'} value={languageCode}
                    defaultChecked={this.props.defaultLanguages.indexOf(languageCode) !== -1} />
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
                  <li><label htmlFor={languageCode + '_language-switch'}
                    onClick={this.switchLanguage}>{languageCode}</label></li>
                )
              })
            }
          </ul>
        </div>
      </div>
    )
  }
})

module.exports.renderLanguageSwitch = function (languages, defaultLanguages, target) {
  ReactDOM.render(
    <LanguageSwitch languages={languages} defaultLanguages={defaultLanguages} />,
    document.getElementById(target)
  )
}
