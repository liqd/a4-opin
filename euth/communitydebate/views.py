from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.filters import views as filter_views
from adhocracy4.modules.models import Module
from euth.projects import mixins as prj_mixins

from . import forms
from . import models as communitydebate_models
from .filters import TopicFilterSet
from .mixins import TopicFormMixin


class TopicListView(prj_mixins.ProjectPhaseMixin,
                    filter_views.FilteredListView):
    model = communitydebate_models.Topic
    paginate_by = 15
    filter_set = TopicFilterSet

    def get_queryset(self):
        return super().get_queryset().filter(module=self.module) \
            .annotate_positive_rating_count() \
            .annotate_negative_rating_count() \
            .annotate_comment_count()


class TopicDetailView(generic.DetailView):
    model = communitydebate_models.Topic
    queryset = \
        communitydebate_models.Topic.objects\
        .annotate_positive_rating_count() \
        .annotate_negative_rating_count()
    permission_required = 'euth_communitydebate.view_topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        upload_files = communitydebate_models.TopicFileUpload.objects\
            .filter(topic=self.object)
        context['upload_files'] = upload_files
        return context


class TopicCreateView(PermissionRequiredMixin, generic.CreateView,
                      TopicFormMixin):
    model = communitydebate_models.Topic
    form_class = forms.TopicForm
    permission_required = 'euth_communitydebate.propose_topic'
    template_name = 'euth_communitydebate/topic_form.html'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def dispatch(self, *args, **kwargs):
        mod_slug = self.kwargs[self.slug_url_kwarg]
        self.module = Module.objects.get(slug=mod_slug)
        self.project = self.module.project
        return super().dispatch(*args, **kwargs)

    def get_permission_object(self, *args, **kwargs):
        return self.module

    def get_context_data(self, upload_forms=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        context['mode'] = 'create'
        if not upload_forms:
            upload_forms = self.empty_upload_formset()
        context['upload_forms'] = upload_forms
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.module = self.module
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['module'] = self.module
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        upload_forms = self.filled_upload_formset(request)
        if form.is_valid() and upload_forms.is_valid():
            response = self.form_valid(form)
            self._process_upload_formdata(upload_forms)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 _('Topic '
                                   'successfully created'))

        else:
            response = render(request,
                              self.template_name,
                              self.get_context_data(upload_forms=upload_forms))
        return response

    def _process_upload_formdata(self, upload_forms):
        with transaction.atomic():
            instances = upload_forms.save(commit=False)
            for instance in instances:
                instance.topic = self.object
                instance.save()


class TopicUpdateView(PermissionRequiredMixin, generic.UpdateView,
                      TopicFormMixin):
    model = communitydebate_models.Topic
    form_class = forms.TopicForm
    permission_required = 'euth_communitydebate.modify_topic'
    template_name = 'euth_communitydebate/topic_form.html'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, upload_forms=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        context['mode'] = 'update'
        if not upload_forms:
            queryset = \
                communitydebate_models.TopicFileUpload.\
                objects.filter(topic=self.get_object())
            upload_forms = self.update_upload_formset(queryset)
        context['upload_forms'] = upload_forms
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['module'] = kwargs.get('instance').module
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        upload_forms = self.filled_upload_formset(request)
        if upload_forms.is_valid() and form.is_valid():
            response = self.form_valid(form)
            self._process_upload_formdata(upload_forms)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 _('Topic successfully '
                                   'updated'))
        else:
            response = render(request,
                              self.template_name,
                              self.get_context_data(upload_forms=upload_forms))
        return response

    def _process_upload_formdata(self, upload_forms):
        with transaction.atomic():
            instances = upload_forms.save(commit=False)
            for obj in upload_forms.deleted_objects:
                obj.delete()
            for instance in instances:
                instance.topic = self.object
                instance.save()


class TopicDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = communitydebate_models.Topic
    success_message = _("Your topic has been deleted")
    permission_required = 'euth_communitydebate.modify_topic'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TopicDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project-detail',
                       kwargs={'slug': self.object.project.slug})
