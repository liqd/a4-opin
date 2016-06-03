from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from . import models
from .permissions import permission_required


def listing(request):
    context = {
        'processes': models.Process.objects.all()
    }
    return render(request, 'process/listing.html', context)


def detail(request, process_name):
    process = get_object_or_404(models.Process, name=process_name)
    phases = process.phase_set.order_by('order')
    context = {
        'process': process,
        'phases': phases,
        'breadcrumbs': [
            ('/', reverse('process-listing')),
            (process.title, None),
        ]
    }
    return render(request, 'process/detail.html', context)
