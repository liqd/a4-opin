from django.contrib import messages
from django.core import exceptions
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views import generic

from euth.modules.models import Module

from . import models


class IdeaDetailView(generic.DetailView):
    model = models.Idea


class IdeaUpdateView(generic.UpdateView):
    model = models.Idea
    fields = ['name', 'description', 'image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        context['mode'] = 'update'
        return context

    def get_object(self):
        qs = super().get_object()
        if self.request.user == qs.creator:
            return qs
        else:
            raise exceptions.PermissionDenied


class IdeaCreateView(generic.CreateView):
    model = models.Idea
    fields = ['name', 'description', 'image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg)
        context['slug'] = slug
        module = Module.objects.get(slug=slug)
        context['project'] = module.project
        context['mode'] = 'create'
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        slug = self.kwargs.get(self.slug_url_kwarg)
        module = Module.objects.get(slug=slug)
        form.instance.module = module
        return super().form_valid(form)


class IdeaDeleteView(generic.DeleteView):
    model = models.Idea
    success_message = _("Your Idea has been deleted")

    def get_object(self):
        qs = super().get_object()
        if self.request.user == qs.creator or self.request.user.is_superuser:
            return qs
        else:
            raise exceptions.PermissionDenied

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(IdeaDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project-detail',
                       kwargs={'slug': self.object.project.slug})
