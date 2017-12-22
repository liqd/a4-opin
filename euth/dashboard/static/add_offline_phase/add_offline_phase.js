/* global django $ */
window.jQuery(document).ready(function () {
  function updateNewElement (element) {
    element.addClass('phaseform-offline-phase')
    element.find('#id_phases-0-type').val('euth_offlinephases:offline')
    element.find('#id_phases-0-delete').val(0)
    element.find('.collapse').eq(0).text(django.gettext('Offline Phase')).append('<i class="fa fa-chevron-up pull-right"></i>')
    element.css('display', 'block')

    var button = getButton(element)
    button.click(function (e) {
      e.preventDefault()
      deletePhase($(e.target).closest('.phase-form'))
    })
  }

  function getButton (element) {
    var buttons = element.find(':input[type=button]')
    if (buttons.length > 0) {
      return $(buttons[0])
    } else {
      var button = $('<button type="button" class="phaseform-delete btn btn-danger"><i class="fa fa-times" aria-hidden="true"></i></button>')
      element.find('.phasefrom-collapse-top').prepend(button)
      return button
    }
  }

  function setNewElementInputValues (element) {
    element.find(':input:not([type=button])').each(function () {
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
  }

  function setPhaseIds () {
    $('.phase-form').each(function (index) {
      var accordion = $(this).find('.collapse')
      accordion.eq(0).attr('href', '#phase-' + index)
      accordion.eq(1).attr('id', 'phase-' + index)

      $(this).find(':input:not([type=button])').each(function () {
        if ($(this).attr('name')) {
          var currentNumber = $(this).attr('name').split('-')[1]
          var currentType = $(this).attr('name').split('-')[2]
          var name = $(this).attr('name').replace('-' + currentNumber + '-', '-' + index + '-')
          var id = 'id_' + name
          $(this).attr({'name': name, 'id': id})
          if (currentType === 'weight') {
            $(this).val(index)
          }
        }
      })
    })
  }

  function cloneMore (selector, type, target) {
    var newElement = $(selector).clone()
    var total = $('#id_' + type + '-TOTAL_FORMS').val()
    updateNewElement(newElement)
    setNewElementInputValues(newElement)

    $(target).after(newElement)
    $(target).remove()

    setPhaseIds()

    total++

    $('#id_' + type + '-TOTAL_FORMS').val(total)
    $('#id_' + type + '-INITIAL_FORMS').val(0)
  }

  function deletePhase (phase) {
    var deleteInput = $(phase).find('[id^="id_phases-"][id$="-delete"]')[0]
    var nameInput = $(phase).find('[id^="id_phases-"][id$="-name"]')[0]
    var descriptionInput = $(phase).find('[id^="id_phases-"][id$="-description"]')[0]
    $(deleteInput).val(1)
    $(nameInput).val('xx')
    $(descriptionInput).val('xx')

    var newElement = $('<a class="add-offline-phase btn btn-gray btn-primary btn-sm" href=""><i class="fa fa-plus"></i>' + django.gettext('add offline phase') + '</a>')
    newElement.click(function (e) {
      e.preventDefault()
      addPhase($(e.target).closest('.add-offline-phase'))
      return false
    })
    $(phase).css('display', 'none')
    $(phase).after(newElement)
  }

  function addPhase (element) {
    var phaseForm = $('.phase-form').first()
    cloneMore(phaseForm, 'phases', element)
  }

  $('.add-offline-phase').click(function (e) {
    e.preventDefault()
    addPhase($(e.target).closest('.add-offline-phase'))
    return false
  })

  $('.phaseform-delete').click(function (e) {
    e.preventDefault()
    deletePhase($(e.target).closest('.phase-form'))
  })
})
