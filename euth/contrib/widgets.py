from django.forms import widgets


class ImageInputWidget(widgets.ClearableFileInput):
    template_with_initial = (
        '%(initial_text)s: <img src="%(initial_url)s" alt="%(initial)s"> '
        '%(clear_template)s<br />%(input_text)s: %(input)s'
    )

    template_with_clear = (
        '%(clear)s <label for="%(clear_checkbox_id)s"> '
        '%(clear_checkbox_label)s</label>'
    )
