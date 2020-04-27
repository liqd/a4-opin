from django.contrib import messages
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
        communitydebate_models.Topic.objects.annotate_positive_rating_count() \
        .annotate_negative_rating_count()
    permission_required = 'euth_communitydebate.view_topic'


class TopicCreateView(PermissionRequiredMixin, generic.CreateView):
    model = communitydebate_models.Topic
    form_class = forms.TopicForm
    permission_required = 'euth_communitydebate.propose_topic'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        context['mode'] = 'create'
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.module = self.module
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['module'] = self.module
        return kwargs


class TopicUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = communitydebate_models.Topic
    form_class = forms.TopicForm
    permission_required = 'euth_communitydebate.modify_topic'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        context['mode'] = 'update'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['module'] = kwargs.get('instance').module
        return kwargs


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
