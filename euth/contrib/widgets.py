from os.path import basename

from django.contrib.staticfiles.storage import staticfiles_storage
from django.forms import widgets
from django.utils import formats
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import get_language, ugettext


class ImageInputWidget(widgets.ClearableFileInput):

    """
    A project-specific improved version of the clearable file upload.

    Allows to upload and delete uploaded files. It doesn't passing attributes
    using the positional `attrs` argument and hard codes css files.
    """
    class Media:
        js = (staticfiles_storage.url('js/imageUploader.js'),)

    def render(self, name, value, attrs=None):

        substitutions = {
            'name': name,
            'filename': '',
            'file_placeholder': ugettext(
                'Select a picture from your local folder.'
            ),
            'post_note': ugettext(
                'You’re image will be uploaded/removed '
                'once you save your changes at the end of this page.'
            ),
            'upload_title': ugettext('Upload a picture'),
            'clear_title': ugettext('Remove the picture'),
        }
        snippets = {
            'name': '{name}',
            'file_input': (
                super(widgets.ClearableFileInput, self).render(name, value, {
                    'id': name,
                    'class': 'form-control form-control-file'
                })
            ),
            'text_input': (
                widgets.TextInput().render('__noname__', '{filename}', {
                    'class': 'form-control form-control-file-dummy',
                    'placeholder': '{file_placeholder}'
                })
            ),
            'alert': (
                '<div class="alert alert-info" role="alert">{post_note}</div>'
            ),
            'img': '',
            'checkbox': '',
        }

        if self.is_initial(value):
            substitutions['url'] = conditional_escape(value.url)
            substitutions['filename'] = basename(value.name)
            snippets['img'] = (
                '<img id="img-{name}" src="{url}" class="img-responsive" '
                ' alt="" />'
            )

            if not self.is_required:
                substitutions['checkbox_id'] = self.clear_checkbox_id(name)
                snippets['button'] = (
                    '<label for="{checkbox_id}" class="btn btn-danger"'
                    'title="{clear_title}"><i class="fa fa-trash"></i></label>'
                )
                snippets['checkbox'] = widgets.CheckboxInput()\
                    .render(self.clear_checkbox_name(name), False,
                            attrs={'id': '{checkbox_id}',
                                   'class': 'clear-image'})
        else:
            snippets['button'] = (
                '<label for="{name}" class="btn btn-default"'
                'title="{upload_title}">'
                '<i class="fa fa-cloud-upload"></i></label>'
            )

        markup = """
        <div class="row">
            <div class="upload-wrapper form-control-upload col-sm-9 col-md-8">
                {text_input}
                <span class="input-group-btn">
                    {button}
                </span>
                {file_input}
                {alert}
            </div>
            <div class="col-sm-3 col-md-4">
                <div class="form-{name}">
                    {checkbox}
                    {img}
                </div>
            </div>
        </div>
        <script>
          uploadPreview("#{name}", "#img-{name}")
        </script>
        """.format(**snippets).format(**substitutions)

        return mark_safe(markup)


class DateTimeInput(widgets.DateTimeInput):

    class Media:
        js = (staticfiles_storage.url('flatpickr.min.js'),
              'js/dateTimeInput.js')
        css = {'all': [staticfiles_storage.url('flatpickr.min.css')]}

    input_type = 'text'

    # becomes a public value in Django 1.10
    def _format_value(self, value):
        return formats.localize_input(value,
                                      formats.get_format(self.format_key)[2])

    def render(self, name, value, attrs=None):
        if attrs:
            format = formats.get_format(self.format_key)[2]
            attrs.update({
                'class': attrs.get('class', '') + ' flatpickr',
                'data-enable-time': 'true',
                'data-time_24hr': 'true',
                'data-language': get_language(),
                'data-date-format': format.replace('%', '').replace('M', 'i'),
            })

            if value:
                attrs.update({
                    'data-default-date': value
                })
        input = mark_safe(super().render(name, value, attrs))
        return input
