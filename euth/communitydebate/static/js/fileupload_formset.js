/* global $ django */
import { showFileName } from '../../../../euth_wagtail/assets/js/euth_wagtail';
(function (init) {
  document.addEventListener('DOMContentLoaded', init, false)
  document.addEventListener('a4.embed.ready', init, false)
})(function () {
  // Dynamically add subforms to a formset.
  const $formsets = $('.js-formset')
  const PLACEHOLDER = /__prefix__/g
  const dynamicFormSets = []

  const DynamicFormSet = function ($formset) {
    this.$formset = $formset
    this.$formTemplate = this.$formset.find('.js-form-template')
    this.prefix = this.$formset.data('prefix')
    this.$totalInput = this.$formset.find('#id_' + this.prefix + '-TOTAL_FORMS')
    this.total = parseInt(this.$totalInput.val())
    this.maxNum = parseInt(this.$formset.find('#id_' + this.prefix + '-MAX_NUM_FORMS').val())

    this.$formset.on('click', '.js-add-form', this.addForm.bind(this))
  }

  DynamicFormSet.prototype.addForm = function () {
    if (this.total < this.maxNum) {
      const id = this.total
      this.total += 1
      this.$totalInput.val(this.total)
      const newForm = getNewForm(this.$formTemplate, id)
      $(newForm).insertBefore(this.$formTemplate)
      document.getElementById(this.prefix + '-' + id.toString() + '-document').addEventListener('change', showFileName, false)
    } else {
      const text = django.gettext('Maximum number of upload documents reached.')
      $('#error-max-num-forms').html('<ul class="errorlist"><li>' + text + '</li></ul>')
    }
  }

  function getNewForm ($formTemplate, id) {
    return $formTemplate.html().replace(PLACEHOLDER, id)
  }

  $formsets.each(function (i) {
    dynamicFormSets.push(
      new DynamicFormSet($formsets.eq(i))
    )
  })
})
