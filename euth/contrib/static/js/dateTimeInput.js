/* global $ */
$('.flatpickr').flatpickr({
  onChange: function (selectedDates, dateStr, instance) {
    var newDate = instance.formatDate(instance.config.dateFormat, selectedDates[0].fp_toUTC())
    $(instance.element).val(newDate)
  },
  onReady: function (selectedDates, dateStr, instance) {
    var newDate = instance.formatDate(instance.config.dateFormat, selectedDates[0].fp_toUTC())
    $(instance.element).val(newDate)
  }
})
