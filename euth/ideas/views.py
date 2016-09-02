from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from euth.modules import mixins as modules_mixins
from euth.modules.models import Module
from euth.projects import mixins

from . import forms, models


class IdeaListView(mixins.ProjectMixin, generic.ListView):
    model = models.Idea

    def get_queryset(self):
        return models.Idea.objects.filter(module=self.module).order_by('name')


class IdeaDetailView(generic.DetailView, modules_mixins.ItemMixin):
    model = models.Idea


class IdeaUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = models.Idea
    form_class = forms.IdeaForm
    permission_required = 'ideas.modify_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        context['mode'] = 'update'
        return context


class IdeaCreateView(PermissionRequiredMixin, generic.CreateView):
    model = models.Idea
    form_class = forms.IdeaForm
    permission_required = 'ideas.create_idea'

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
    model = models.Idea
    success_message = _("Your Idea has been deleted")
    permission_required = 'ideas.create_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(IdeaDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project-detail',
                       kwargs={'slug': self.object.project.slug})
