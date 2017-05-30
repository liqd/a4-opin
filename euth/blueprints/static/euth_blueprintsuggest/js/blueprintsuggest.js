/* global jQuery django */
(function ($) {
  var blueprintsuggest = {
    init: function () {
      this.$aim = $('input[name="aim"]')
      this.$experience = $('input[name="experience"]')
      this.$result = $('input[name="result"]')
      this.$motivation = $('input[name="motivation"]')
      this.$scope = $('input[name="scope"]')
      this.$duration = $('input[name="duration"]')
      this.$participants = $('input[name="participants"]')
      this.$accessibility = $('input[name="accessibility"]')
      this.$form = $('.blueprintsuggest')

      $('.js-continue').on('click', this.clickContinueHandler.bind(this))
      $('.js-back').on('click', this.clickBackHandler)
      $('.js-send').on('click', this.clickSendHandler.bind(this))
    },

    clickContinueHandler: function (e) {
      var $this = $(e.target)
      var $tab = $this.parents('.tab-pane')
      var $checked = this.$aim.filter(':checked')

      // remove old errorlist
      $tab.find('.errorlist').remove()

      if (!$checked.length) {
        // there's no radio button checked, not valid, so add new errorlist
        var text = django.gettext('Please pick an aim for your project.')
        $tab.find('.dst-lightbox-progress').before(this.getErrorElement(text))
        return true
      }

      $tab.removeClass('active').next().addClass('active')

      return false
    },

    clickSendHandler: function (e) {
      var $this = $(e.target)
      var $tab = $this.parents('.tab-pane')
      var $checkedExperience = this.$experience.filter(':checked')
      var $checkedResult = this.$result.filter(':checked')
      var $checkedMotivation = this.$motivation.filter(':checked')
      var $checkedDuration = this.$duration.filter(':checked')
      var $checkedParticipants = this.$participants.filter(':checked')
      var $checkedScope = this.$scope.filter(':checked')
      var $checkedAccessibility = this.$accessibility.filter(':checked')

      // remove old errorlist
      $tab.find('.errorlist').remove()

      if (!$checkedExperience.length ||
          !$checkedResult.length ||
          !$checkedMotivation.length ||
          !$checkedDuration.length ||
          !$checkedScope.length ||
          !$checkedParticipants.length ||
          !$checkedAccessibility.length) {
        // there is some radio button not checked, not valid, so add new errorlist
        var text = django.gettext('Please set all values for your project.')
        $tab.find('.dst-lightbox-progress').before(this.getErrorElement(text))
        e.preventDefault()
        return false
      }

      return true
    },

    getErrorElement: function (text) {
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
