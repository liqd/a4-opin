window.jQuery(document).ready(function () {
  var $ = window.jQuery

  function cloneMore (selector, type, target) {
    var newElement = $(selector).clone(true)
    var total = $('#id_' + type + '-TOTAL_FORMS').val()

    newElement.find('#id_phases-0-type').val('euth_offlinephases:000:offline')
    newElement.find('.collapse').eq(0).text('Offline Phase ').append('<i class="fa fa-chevron-up pull-right"></i>')

    var accordion = newElement.find('.collapse')
    accordion.eq(0).attr('href', '#phase-' + (parseInt(total) + 1))
    accordion.eq(1).attr('id', 'phase-' + (parseInt(total) + 1))

    newElement.find(':input').each(function () {
      var currentType = $(this).attr('name').split('-')[2]
      if (currentType !== 'type') {
        $(this).val('')
      }
      if (currentType === 'start_date' || currentType === 'end_date') {
        $(this).flatpickr()
      }
      if (currentType === 'id') {
        $(this).removeAttr('value')
      }
    })

    $(target).after(newElement)
    $(target).remove()

    $('.phase-form').each(function (index) {
      $(this).find(':input').each(function () {
        var currentNumber = $(this).attr('name').split('-')[1]
        var currentType = $(this).attr('name').split('-')[2]
        var name = $(this).attr('name').replace('-' + currentNumber + '-', '-' + index + '-')
        var id = 'id_' + name
        $(this).attr({'name': name, 'id': id})
        if (currentType === 'weight') {
          $(this).val(index)
        }
      })
    })

    total++

    $('#id_' + type + '-TOTAL_FORMS').val(total)
    $('#id_' + type + '-INITIAL_FORMS').val(0)
  }

  $('.add-offline-phase').click(function (e) {
    e.preventDefault()
    var phaseForm = $('.phase-form').first()
    cloneMore(phaseForm, 'phases', e.target)
    return false
  })
})
