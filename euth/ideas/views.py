from django.contrib.messages import views
from django.core import exceptions
from django.shortcuts import render
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
