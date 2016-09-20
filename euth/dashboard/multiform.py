import multiform
from django.forms import formsets


class MultiModelForm(multiform.MultiModelForm):

    def __init__(self, *args, **kwargs):
        """
        Filter our arguments that don't make sense for formsets as base_forms.
        Should be moved to multiforms itself.
        """
        base_forms = self.get_base_forms()
        formset_names = [name for name, form in base_forms.items()
                         if issubclass(form, formsets.BaseFormSet)]

        invalid_formset_kwargs = [
            'instance', 'empty_permitted', 'label_suffix'
        ]

        def filter_function(name, value):
            if name in formset_names:
                return multiform.InvalidArgument
            else:
                return value

        for kwarg in invalid_formset_kwargs:
            setattr(self, 'dispatch_init_{}'.format(kwarg), filter_function)

        return super().__init__(*args, **kwargs)

    def _combine(self, *args, **kwargs):
        """
        Filter out list of falsy values which occour when using formsets.
        Should be moved to multiforms itself.

        WARNING: This kind of hacky. It should be better fixed somewhere else.
        """
        values = super()._combine(*args, **kwargs)
        if 'filter' in kwargs and kwargs['filter']:
            values = [
                value for value in values
                if not hasattr(value, '__iter__') or not any(value)
            ]
        return values

    def full_clean(self):
        """
        Modified full clean that does collect cleaned data from formsets.
        Should be moved to multiforms itself.
        """
        self._errors = self._combine('errors', filter=True)
        base_forms = self.get_base_forms()

        if not self._errors:
            self.cleaned_data = {}
            for name, formset in self.forms.items():
                if issubclass(base_forms[name], formsets.BaseFormSet):
                    self.cleaned_data[name] = [f.cleaned_data for f in formset]
