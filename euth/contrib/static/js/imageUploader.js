window.uploadPreview = function (srcInput, targetImg, deleteInput) {
  var $ = window.jQuery
  var input = $(srcInput)
  var readUrl = function () {
    var domInput = input[0]
    if (domInput.files && domInput.files[0]) {
      if (window.FileReader) {
        var reader = new window.FileReader()
        reader.onload = function (e) {
          $(targetImg).attr('src', e.target.result)
          $(deleteInput).prop('checked', false)
        }
        reader.readAsDataURL(domInput.files[0])
      } else {
        $(deleteInput).prop('checked', false)
      }
    }
  }
  input.change(readUrl)
}
