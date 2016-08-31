from os.path import basename

from django.forms import widgets
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext


class ImageInputWidget(widgets.ClearableFileInput):
    def render(self, name, value, attrs=None):
        file_input = super(widgets.ClearableFileInput, self)\
            .render(name, value, attrs)

        substitutions = {
            'filename': '',
            'file_placeholder': ugettext(
                'Select a picture from your local folder.'
            ),
            'post_note': ugettext(
                'Please hit the post button to save your changes.'
            ),
            'upload_title': ugettext('Upload a picture'),
            'clear_title': ugettext('Remove the picture'),
        }
        snippets = {
            'text_input': (
                '<input type="text"'
                'class="form-control form-control-file-dummy"'
                'value="{filename}" placeholder="{file_placeholder}">'
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
                '<img src="{url}" class="img-responsive" alt="" />'
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
                '<label for="id_image" class="btn btn-default"'
                'title="{upload_title}">'
                '<i class="fa fa-cloud-upload"></i></label>'
            )

        markup = """
        <div class="upload-wrapper">
            {text_input}
            <span class="input-group-btn">
                {button}
            </span>
            {alert}
        </div>
        {checkbox}
        {img}
        """.format(**snippets).format(**substitutions)

        return mark_safe(markup + file_input)
