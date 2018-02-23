from os.path import basename

from django.forms import widgets
from django.template import loader
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext


class FileUploadWidget(widgets.ClearableFileInput):
    def render(self, name, value, attrs=None):
        has_file_set = self.is_initial(value)
        is_required = self.is_required

        file_placeholder = ugettext('Select a file from your local folder.')
        file_input = super().render(name, None, {
            'id': name,
            'class': 'form-control form-control-file'
        })

        if has_file_set:
            file_name = basename(value.name)
            file_url = conditional_escape(value.url)
        else:
            file_name = ""
            file_url = ""

        text_input = widgets.TextInput().render('__noname__', file_name, {
            'class': 'form-control form-control-file-dummy',
            'placeholder': file_placeholder
        })

        checkbox_id = self.clear_checkbox_id(name)
        checkbox_name = self.clear_checkbox_name(name)
        checkbox_input = widgets.CheckboxInput().render(checkbox_name, False, {
            'id': checkbox_id,
            'class': 'clear-image',
            'data-upload-clear': name,
        })

        context = {
            'name': name,
            'has_image_set': has_file_set,
            'is_required': is_required,
            'file_url': file_url,
            'file_input': file_input,
            'file_id': name + '-file',
            'text_input': text_input,
            'checkbox_input': checkbox_input,
            'checkbox_id': checkbox_id
        }

        return mark_safe(
            loader.render_to_string(
                'euth_offlinephases/file_upload_widget.html',
                context
            )
        )

    def value_from_datadict(self, data, files, name):
        file_value = super(widgets.ClearableFileInput, self) \
            .value_from_datadict(data, files, name)
        checkbox_value = widgets.CheckboxInput() \
            .value_from_datadict(data, files, self.clear_checkbox_name(name))
        if not self.is_required and checkbox_value:
            return False
        return file_value
