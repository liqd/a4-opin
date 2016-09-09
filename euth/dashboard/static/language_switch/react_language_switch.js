var React = require('react')
var ReactDOM = require('react-dom')
var h = require('react-hyperscript')
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
      h('div', [
        h('ul.checkbox-list', {ref: 'checkboxList'}, this.props.languages.map(function (languageCode, i) {
          return h('li' + (i === 0 ? '.active' : ''), [
            h('input', {
              type: 'checkbox',
              id: languageCode + '_language-switch',
              value: languageCode,
              defaultChecked: i < 3
            }),
            h('a.language-switch.btn', {
              href: '#' + languageCode + '_language_panel',
              'data-toggle': 'tab'
            }, languageCode)
          ])
        })),
        h('div.dropdown', [
          h('button.btn.btn-default.dropdown-toggle', {
            type: 'button',
            ref: 'toggleButton',
            'data-toggle': 'dropdown'
          }, [
            h('i.fa.fa-plus')
          ]),
          h('ul.dropdown-menu', this.props.languages.map(function (languageCode) {
            return h('li', [
              h('label', {
                htmlFor: languageCode + '_language-switch',
                onClick: this.switchLanguage.bind(this)
              }, languageCode)
            ])
          }.bind(this)))
        ])
      ])
    )
  }
})

module.exports.renderLanguageSwitch = function (languages, target) {
  ReactDOM.render(
    h(LanguageSwitch, {
      languages: languages
    }),
    document.getElementById(target))
}
