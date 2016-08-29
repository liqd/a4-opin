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
            'filename': basename(value.name),
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
            if not self.is_required:
                snippets['button'] = (
                    '<label for="image-clear_id" class="btn btn-danger"'
                    'title="{clear_title}"><i class="fa fa-trash"></i></label>'
                )
                snippets['checkbox'] = widgets.CheckboxInput()\
                    .render('image-clear', False,
                            attrs={'id': 'image-clear_id',
                                   'class': 'clear-image'})
            snippets['img'] = (
                '<img src="{url}" class="img-responsive" alt="" />'
            )
            substitutions['url'] = conditional_escape(value.url)
        elif not self.is_initial(value):
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
            {checkbox}
        </div>
        {img}
        """.format(**snippets).format(**substitutions)

        return mark_safe(markup + file_input)
