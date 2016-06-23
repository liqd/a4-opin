from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Process


class ProcessListView(ListView):
    model = Process


class ProcessDetailView(DetailView):
    model = Process
    slug_url_kwarg = 'process_slug'

    def get_context_data(self, **kwargs):
        context = super(ProcessDetailView, self).get_context_data(**kwargs)
        context['phases'] = context['process'].phases
        return context
