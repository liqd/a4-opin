window.jQuery(document).ready(function () {
  var $ = window.jQuery

  function cloneMore (selector, type, target) {
    var newElement = $(selector).clone(true)
    var total = $('#id_' + type + '-TOTAL_FORMS').val()

    newElement.find('#id_phases-0-type').val('euth_offlinephases:000:offline')
    newElement.find('.collapse').eq(0).text('Offline Phase ').append('<i class="fa fa-chevron-up pull-right"></i>')

    $(target).after(newElement)
    $(target).remove()

    $('.phase-form').each(function (index) {
      var accordion = $(this).find('.collapse')
      accordion.eq(0).attr('href', '#phase-' + index)
      accordion.eq(1).attr('id', 'phase-' + index)

      $(this).find(':input').each(function () {
        var currentNumber = $(this).attr('name').split('-')[1]
        var name = $(this).attr('name').replace('-' + currentNumber + '-', '-' + index + '-')
        var id = 'id_' + name
        $(this).attr({'name': name, 'id': id})
      })
    })

    total++

    $('#id_' + type + '-TOTAL_FORMS').val(total)

    $('.flatpickr').flatpickr()
  }

  $('.add-offline-phase').click(function (e) {
    e.preventDefault()
    var phaseForm = $('.phase-form').first()
    cloneMore(phaseForm, 'phases', e.target)
    return false
  })
})
