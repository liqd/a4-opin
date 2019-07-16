/* global jQuery django */
(function ($) {
  var blueprintsuggest = {
    init: function () {
      $('.js-continue').on('click', this.clickContinueHandler.bind(this))
      $('.js-back').on('click', this.clickBackHandler)
      $('.js-send').on('click', this.clickSendHandler.bind(this))
    },

    validate: function ($tab) {
      /*
       * Ensure that for each group of radio buttons in $tab at least one is checked.
       */
      var $radioButtons = $tab.find('input[type=radio]')
      var radioButtonsByName = {}
      $radioButtons.map(function () {
        var $this = $(this)
        var name = $this.attr('name')

        if (!Object.prototype.hasOwnProperty.call(radioButtonsByName, name)) {
          radioButtonsByName[name] = $()
        }

        radioButtonsByName[name] = radioButtonsByName[name].add($this)
      })

      for (var key in radioButtonsByName) {
        if (Object.prototype.hasOwnProperty.call(radioButtonsByName, key)) {
          var $inputs = radioButtonsByName[key]
          if (!$inputs.filter(':checked').length) {
            return false
          }
        }
      }

      return true
    },

    clickContinueHandler: function (e) {
      var $this = $(e.target)
      var $tab = $this.parents('.tab-pane')
      var isValid = this.validate($tab)

      // remove old errorlist
      $tab.find('.errorlist').remove()

      if (!isValid) {
        // there's no radio button checked, not valid, so add new errorlist
        $tab.find('.dst-lightbox-progress').before(this.getErrorElement())
        return true
      }

      $tab.removeClass('active').next().addClass('active')
      return false
    },

    clickSendHandler: function (e) {
      var $this = $(e.target)
      var $tab = $this.parents('.tab-pane')
      var isValid = this.validate($tab)

      // remove old errorlist
      $tab.find('.errorlist').remove()

      if (!isValid) {
        // there is some radio button not checked, not valid, so add new errorlist
        $tab.find('.dst-lightbox-progress').before(this.getErrorElement())
        e.preventDefault()
        return false
      }

      return true
    },

    getErrorElement: function () {
      var text = django.gettext('Please set all values for your project.')
      return '<ul class="errorlist"><li>' + text + '</li></ul>'
    },

    clickBackHandler: function () {
      var $tab = $(this).parents('.tab-pane')
      $tab.removeClass('active').prev().addClass('active')
    }
  }

  $(function () {
    blueprintsuggest.init()
  })
}(jQuery))
