/* global django */
(function ($) {
  const blueprintsuggest = {
    init: function () {
      $('.js-continue').on('click', this.clickContinueHandler.bind(this))
      $('.js-back').on('click', this.clickBackHandler)
      $('.js-send').on('click', this.clickSendHandler.bind(this))
    },

    validate: function ($tab) {
      /*
       * Ensure that for each group of radio buttons in $tab at least one is checked.
       */
      const $radioButtons = $tab.find('input[type=radio]')
      const radioButtonsByName = {}
      $radioButtons.map(function () {
        const $this = $(this)
        const name = $this.attr('name')

        if (!Object.prototype.hasOwnProperty.call(radioButtonsByName, name)) {
          radioButtonsByName[name] = $()
        } else {
          radioButtonsByName[name] = radioButtonsByName[name].add($this)
        }
        return radioButtonsByName[name]
      })

      for (const key in radioButtonsByName) {
        if (Object.prototype.hasOwnProperty.call(radioButtonsByName, key)) {
          const $inputs = radioButtonsByName[key]
          if (!$inputs.filter(':checked').length) {
            return false
          }
        }
      }

      return true
    },

    clickContinueHandler: function (e) {
      const $this = $(e.target)
      const $tab = $this.parents('.tab-pane')
      const isValid = this.validate($tab)

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
      const $this = $(e.target)
      const $tab = $this.parents('.tab-pane')
      const isValid = this.validate($tab)

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
      const text = django.gettext('Please set all values for your project.')
      return '<ul class="errorlist"><li>' + text + '</li></ul>'
    },

    clickBackHandler: function () {
      const $tab = $(this).parents('.tab-pane')
      $tab.removeClass('active').prev().addClass('active')
    }
  }

  $(function () {
    blueprintsuggest.init()
  })
}(jQuery))
