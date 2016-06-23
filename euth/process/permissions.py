from functools import wraps
from django.http import HttpResponseForbidden

from .models import Process


def permission_required(perm):
    def decorator(view_func):
        @wraps(view_func)
        def _wrap_view(request, *args, **kwargs):
            process_slug = kwargs.get("process_slug")
            if not process_slug:
                raise Exception(
                    "No process_slug given, can't determine process")
            process = Process.objects.get(slug=process_slug)
            active_phase = process.get_current_phase()
            is_participant = process.participants.filter(
                id=request.user.id).first() is not None
            is_moderator = process.moderators.filter(
                id=request.user.id).first() is not None

            if not active_phase:
                return HttpResponseForbidden()
            elif is_moderator and active_phase.phase_type.moderator_permissions.filter(codename=perm).first():
                return view_func(request, *args, **kwargs)
            elif is_participant and active_phase.phase_type.participant_permissions.filter(codename=perm).first():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()
        return _wrap_view
    return decorator
