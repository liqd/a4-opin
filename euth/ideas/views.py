from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.filters import views as filter_views
from adhocracy4.modules.models import Module
from euth.projects import mixins as prj_mixins

from . import forms
from . import models as idea_models
from .filters import IdeaFilterSet


class IdeaListView(
    prj_mixins.ProjectPhaseMixin,
    filter_views.FilteredListView
):
    model = idea_models.Idea
    paginate_by = 15
    filter_set = IdeaFilterSet

    def get_queryset(self):
        return super().get_queryset().filter(module=self.module) \
            .annotate_positive_rating_count() \
            .annotate_negative_rating_count() \
            .annotate_comment_count()


class IdeaDetailView(PermissionRequiredMixin, generic.DetailView):
    model = idea_models.Idea
    queryset = idea_models.Idea.objects.annotate_positive_rating_count() \
        .annotate_negative_rating_count()
    permission_required = 'euth_ideas.view_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_is_moderator'] = self.object.creator in self.object. \
            project.moderators.all()
        return context


class IdeaUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = idea_models.Idea
    form_class = forms.IdeaForm
    permission_required = 'euth_ideas.modify_idea'

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


class IdeaCreateView(PermissionRequiredMixin, generic.CreateView):
    model = idea_models.Idea
    form_class = forms.IdeaForm
    permission_required = 'euth_ideas.propose_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def dispatch(self, *args, **kwargs):
        mod_slug = self.kwargs[self.slug_url_kwarg]
        self.module = get_object_or_404(Module, slug=mod_slug)
        self.project = self.module.project
        return super().dispatch(*args, **kwargs)

    def get_permission_object(self, *args, **kwargs):
        return self.module

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.module.slug
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


class IdeaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = idea_models.Idea
    success_message = _("Your Idea has been deleted")
    permission_required = 'euth_ideas.modify_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(IdeaDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project-detail',
                       kwargs={'slug': self.object.project.slug})
