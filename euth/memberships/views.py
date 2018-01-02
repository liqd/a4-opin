from django.http import Http404
from django.shortcuts import redirect
from django.views import generic
from rules.compat import access_mixins as mixin
from rules.contrib import views as rules_views

from adhocracy4.projects import models as prj_models
from euth.projects import mixins as prj_mixins

from . import forms, models


class RequestsProjectDetailView(
    rules_views.PermissionRequiredMixin,
    prj_mixins.PhaseDispatchMixin,
    generic.DetailView
):
    model = prj_models.Project
    permission_required = 'a4projects.view_project'
    project_url_kwarg = 'slug'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    @property
    def project(self):
        """
        Emulate ProjectMixin interface for template sharing.
        """
        return self.get_object()

    def handle_no_permission(self):
        """
        Check if user could join
        """
        user = self.request.user
        is_member = user.is_authenticated() and self.project.has_member(user)

        if is_member:
            return super().handle_no_permission()
        else:
            return self.handle_no_membership()

    def handle_no_membership(self):
        membership_impossible = (
            not self.request.user.is_authenticated()
            or self.project.is_draft
            or self.project.has_member(self.request.user)
        )

        if membership_impossible:
            return super().handle_no_permission()
        else:
            return redirect('memberships-request',
                            project_slug=self.project.slug)


class InviteDetailView(generic.DetailView):
    model = models.Invite
    slug_field = 'token'
    slug_url_kwarg = 'invite_token'

    def dispatch(self, request, invite_token, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(
                'membership-invite-update',
                invite_token=invite_token
            )
        else:
            return super().dispatch(request, *args, **kwargs)


class InviteUpdateView(mixin.LoginRequiredMixin, generic.UpdateView):
    model = models.Invite
    form_class = forms.InviteForm
    slug_field = 'token'
    slug_url_kwarg = 'invite_token'

    def form_valid(self, form):
        if form.is_accepted():
            form.instance.accept(self.request.user)
            return redirect(form.instance.project.get_absolute_url())
        else:
            form.instance.reject()
            return redirect('/')


class RequestView(mixin.LoginRequiredMixin, generic.DetailView):
    """
    Displays membership request if it exists or allows to create one.
    """
    model = models.Request
    slug_field = 'project__slug'
    slug_url_kwarg = 'project_slug'
    context_object_name = 'join_request'

    def get_queryset(self):
        return self.model.objects.filter(creator=self.request.user)

    def get(self, request, *args, **kwargs):
        if self.project.has_member(request.user):
            return redirect(self.project.get_absolute_url())
        else:
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        project = self.project
        models.Request.objects.request_membership(project, user)
        return redirect(self.request.path)

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None

    @property
    def project(self):
        project_slug = self.kwargs[self.slug_url_kwarg]
        return prj_models.Project.objects.get(slug=project_slug)
