(function ($) {
  var userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone
  $('#id_timezone').val(userTimezone)
})(window.jQuery)
