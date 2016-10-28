window.uploadPreview = function (srcInput, targetImg) {
  var $ = window.jQuery
  var input = $(srcInput)
  var readUrl = function () {
    var domInput = input[0]
    if (domInput.files && domInput.files[0]) {
      var reader = new window.FileReader()
      reader.onload = function (e) {
        $(targetImg).attr('src', e.target.result)
      }
      reader.readAsDataURL(domInput.files[0])
    }
  }
  input.change(readUrl)
}
