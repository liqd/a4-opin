/* global jQuery django */
(function ($) {
  var blueprintsuggest = {
    init: function () {
      this.$aim = $('[name="aim"]')
      this.$form = $('.blueprintsuggest')

      $('.js-continue').on('click', this.clickContinueHandler.bind(this))
      $('.js-back').on('click', this.clickBackHandler)
    },

    clickContinueHandler: function (e) {
      var $this = $(e.target)
      var $tab = $this.parents('.tab-pane')
      var $checked = this.$aim.filter(':checked')

      // remove old errorlist
      $tab.find('.errorlist').remove()

      if (!$checked.length) {
        // there's no radio button checked, not valid, so add new errorlist
        $tab.find('.progress').before(this.getErrorElement())
        return true
      }

      var val = $checked.val()
      if (val >= 4) {
        e.preventDefault()
        this.$form.submit()
      } else {
        $tab.removeClass('active').next().addClass('active')
      }
    },

    getErrorElement: function () {
      var text = django.gettext('Please pick an aim for your project.')
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
