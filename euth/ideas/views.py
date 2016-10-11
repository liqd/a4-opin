from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from euth.modules.models import Module
from euth.projects import mixins

from . import models as idea_models
from . import forms


class IdeaListView(mixins.ProjectMixin, generic.ListView):
    model = idea_models.Idea

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        qs = idea_models.Idea.objects.filter(module=self.module)
        if sort:
            if sort == 'ratings':
                qs = qs.annotate(ratings__count=models.Count(
                    models.Case(
                        models.When(ratings__value=1, then=1),
                        output_field=models.IntegerField()
                    ),
                ))
                return qs.order_by('-ratings__count')
            else:
                try:
                    idea_models.Idea._meta.get_field_by_name(sort)
                    return qs.order_by(sort)
                except models.FieldDoesNotExist:
                    return qs.order_by('name')

        else:
            return qs.order_by('name')


class IdeaDetailView(PermissionRequiredMixin, generic.DetailView):
    model = idea_models.Idea
    permission_required = 'euth_ideas.view_idea'


class IdeaUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = idea_models.Idea
    form_class = forms.IdeaForm
    permission_required = 'euth_ideas.modify_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        context['mode'] = 'update'
        return context


class IdeaCreateView(PermissionRequiredMixin, generic.CreateView):
    model = idea_models.Idea
    form_class = forms.IdeaForm
    permission_required = 'euth_ideas.propose_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def dispatch(self, *args, **kwargs):
        mod_slug = self.kwargs[self.slug_url_kwarg]
        self.module = Module.objects.get(slug=mod_slug)
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


class IdeaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = idea_models.Idea
    success_message = _("Your Idea has been deleted")
    permission_required = 'euth_ideas.modify_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(IdeaDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project-detail',
                       kwargs={'slug': self.object.project.slug})
