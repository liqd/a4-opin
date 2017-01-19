window.jQuery(document).ready(function () {
  var $ = window.jQuery

  function cloneMore (selector, type, target) {
    var newElement = $(selector).clone()
    var total = $('#id_' + type + '-TOTAL_FORMS').val()

    newElement.find('#id_phases-0-type').val('euth_offlinephases:000:offline')
    newElement.find('.collapse').eq(0).text('Offline Phase ').append('<i class="fa fa-chevron-up pull-right"></i>')
    newElement.find('.update-offline-documentation').remove()

    newElement.find(':input').each(function () {
      var currentType = $(this).attr('name').split('-')[2]
      if (currentType !== 'type' && currentType !== 'delete') {
        $(this).val('')
      }
      if (currentType === 'start_date' || currentType === 'end_date') {
        $(this).attr('data-default-date', '')
        $(this).val('')
        $(this).flatpickr()
      }
      if (currentType === 'id') {
        $(this).removeAttr('value')
      }
    })

    $(target).after(newElement)
    $(target).remove()

    $('.phase-form').each(function (index) {
      var accordion = $(this).find('.collapse')
      accordion.eq(0).attr('href', '#phase-' + index)
      accordion.eq(1).attr('id', 'phase-' + index)

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

  function deletePhase (phase) {
    var input = $(phase).find('[id^="id_phases-"][id$="-delete"]')[0]
    $(input).val(1)
    var newElement = $('<a class="add-offline-phase btn btn-gray btn-primary btn-sm" href=""><i class="fa fa-plus"></i>add offline phase</a>')
    newElement.click(function (e) {
      e.preventDefault()
      var phaseForm = $('.phase-form').first()
      cloneMore(phaseForm, 'phases', e.target)
      return false
    })
    $(phase).after(newElement)
    $(phase).css('display', 'none')
  }

  $('.add-offline-phase').click(function (e) {
    e.preventDefault()
    var phaseForm = $('.phase-form').first()
    cloneMore(phaseForm, 'phases', e.target)
    return false
  })

  $('.delete-offline-phase').click(function (e) {
    e.preventDefault()
    deletePhase(e.target.parentElement)
  })
})
