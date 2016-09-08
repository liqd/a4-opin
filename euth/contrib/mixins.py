class TranslatableModelFormsMixin():

    translated_form_class = None
    translated_form_languages = []

    def get_translated_forms(self):
        """
        Create instances for all from classes.
        """
        form_class = self.translated_form_class
        kwargs = self.get_translated_forms_kwargs()
        forms = [
            (prefix, form_class(**kwargs[prefix]))
            for prefix in self.translated_form_languages
        ]
        for lang_code, form in forms:
            form.language_code = lang_code
        return forms

    def get_translated_forms_kwargs(self):
        kwargs = {}

        for form_prefix in self.translated_form_languages:
            kwargs[form_prefix] = {
                'initial': self.initial.get(form_prefix, {}),
                'prefix': form_prefix
            }
            if hasattr(self, 'object'):
                instance = self.object
                translated_instance = instance.__class__.objects.language(
                    form_prefix).get(pk=instance.pk)
                kwargs[form_prefix].update({
                    'instance': translated_instance
                })
            if self.request.method in ('POST', 'PUT'):
                kwargs[form_prefix].update({
                    'data': self.request.POST,
                    'files': self.request.FILES,
                })
        return kwargs

    def get_context_data(self, **kwargs):
        """
        Insert the form into the context dict.
        """
        if 'translated_forms' not in kwargs:
            kwargs['translated_forms'] = self.get_translated_forms()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        forms = form.translated_forms
        for code, form in forms:
            form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        translated_forms = self.get_translated_forms()
        submitted_languages = [lang for lang in self.translated_form_languages
                               if request.POST[lang]]
        forms_valid = all([form.is_valid() for code, form in translated_forms
                           if code in submitted_languages])

        form = self.get_form()
        setattr(form, 'translated_forms', [
            (code, f) for code, f in translated_forms
            if code in submitted_languages
        ])

        if form.is_valid() and forms_valid:
            return self.form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(
                    form=form, translated_forms=translated_forms
                )
            )
