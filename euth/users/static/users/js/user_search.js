var $ = require('jquery')

class UserSearch {
  constructor (typeaheadElem) {
    this.element = typeaheadElem
    this.$element = $(typeaheadElem)
    this.identifier = this.$element.data('identifier')

    this.$element.typeahead({
      hint: true,
      highlight: true,
      minLength: 1
    }, {
      name: 'users',
      source: this.findMatches,
      display: this.getDisplay,
      templates: {
        suggestion: this.renderSuggestions
      }
    })
    // Announce select only if there's an identifier, otherwise it's not needed.

    if (this.identifier) {
      this.$element.on('typeahead:select', this.selectHandler.bind(this))
    }
  }

  renderSuggestions (context) {
    const avatar = context.avatar ? context.avatar : context.default_avatar
    return (
      `<div>
        <img src="${avatar}" alt="" class="circled"> ${context.username}
      </div>`
    )
  }

  findMatches (q, cb, acb) {
    $.get('/api/users?search=' + q, function (results) {
      acb(results)
    })
  }

  getDisplay (context) {
    return context.username
  }

  selectHandler (event, context) {
    if (window.adhocracy4 && window.adhocracy4.userList && window.adhocracy4.userList[this.identifier]) {
      var listeningComponents = window.adhocracy4.userList[this.identifier]
      for (var i = 0; i < listeningComponents.length; i++) {
        const userList = listeningComponents[i]
        userList.add(context).done((data, status) => {
          if (status !== 'success') {
            return console.error(data, status)
          }
          this.$element.typeahead('val', '')
        })
      }
    }
  }
}

$(function () {
  var typeaheadElems = document.querySelectorAll('.typeahead')
  var length = typeaheadElems.length
  var userSearchs = []
  for (var i = 0; i < length; i++) {
    var elem = typeaheadElems[i]
    userSearchs.push(new UserSearch(elem))
  }
})
