from django import forms
from django.contrib import messages
from django.contrib.auth import mixins as mixin
from django.http import Http404
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from rules.contrib import views as rules_views

from adhocracy4.dashboard import mixins
from adhocracy4.projects import models as prj_models
from adhocracy4.projects.mixins import ProjectMixin
from euth.projects import mixins as prj_mixins
from euth.users import models as user_models

from . import forms as membership_forms
from . import models as membership_models


class InviteDashboardView(
    ProjectMixin,
    mixins.DashboardBaseMixin,
    mixins.DashboardComponentMixin,
    generic.detail.SingleObjectMixin,
    generic.FormView
):
    model = prj_models.Project
    fields = []
    permission_required = 'a4projects.change_project'
    project_url_kwarg = 'project_slug'
    template_name = 'euth_memberships/dashboard_invites.html'
    form_class = membership_forms.ProjectInviteForm

    def get_permission_object(self):
        return self.project

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.project

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['project'] = self.object
        return kwargs

    def process_invites(self, invite_formset):
        for form in invite_formset:
            if form.is_valid():
                data = form.cleaned_data
                if 'delete' in data and data['delete']:
                    form.instance.delete()

    def post(self, request, *args, **kwargs):
        if 'submit_action' in request.POST:
            if request.POST['submit_action'] == 'remove_invites':
                MembershipInviteFormset = forms.modelformset_factory(
                    membership_models.Invite,
                    membership_forms.InviteModerationForm,
                    extra=0)
                form_set = MembershipInviteFormset(request.POST)
                self.process_invites(form_set)
                messages.add_message(request,
                                     messages.SUCCESS,
                                     _('Project member invites '
                                       'have been updated'))
            response = redirect(self.get_success_url())
        else:
            response = super().post(request, *args, **kwargs)
        return response

    @property
    def formset(self):
        membership_invites = \
            membership_models.Invite.objects.filter(project=self.project)
        MembershipInviteFormset = forms.modelformset_factory(
            membership_models.Invite,
            membership_forms.InviteModerationForm,
            extra=0)
        return MembershipInviteFormset(queryset=membership_invites)

    def form_valid(self, form):
        emails = form.cleaned_data['emails']
        user = self.request.user
        project = self.object
        for email in emails:
            membership_models.Invite.objects.invite(user, project, email)
        messages.add_message(self.request,
                             messages.SUCCESS,
                             _('Invites have been sent'))
        return super().form_valid(form)

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated


class MembershipsDashboardView(
    ProjectMixin,
    mixins.DashboardBaseMixin,
    mixins.DashboardComponentMixin,
    generic.TemplateView
):
    model = prj_models.Project
    fields = []
    permission_required = 'a4projects.change_project'
    project_url_kwarg = 'project_slug'
    template_name = 'euth_memberships/dashboard_members.html'

    def get_permission_object(self):
        return self.project

    def get_object(self, queryset=None):
        return self.project

    @property
    def membership_request_form(self):
        membership_requests = \
            membership_models.Request.objects.filter(project=self.project)
        MembershipRequestFormset = forms.modelformset_factory(
            membership_models.Request,
            membership_forms.RequestModerationForm,
            extra=0)
        return MembershipRequestFormset(queryset=membership_requests)

    @property
    def member_delete_form(self):
        members = self.project.participants.all()
        MemberFormset = forms.modelformset_factory(
            user_models.User,
            membership_forms.ParticipantsModerationForm,
            extra=0)
        return MemberFormset(queryset=members)

    def process_requests(self, data):
        MembershipRequestFormset = forms.modelformset_factory(
            membership_models.Request,
            membership_forms.RequestModerationForm,
            extra=0)
        for form in MembershipRequestFormset(data):
            if form.is_valid():
                if form.cleaned_data['action'] == 'accept':
                    form.instance.accept()
                if form.cleaned_data['action'] == 'decline':
                    form.instance.decline()

    def process_members(self, data):
        MemberFormset = forms.modelformset_factory(
            user_models.User,
            membership_forms.ParticipantsModerationForm,
            extra=0)
        for form in MemberFormset(data):
            if form.is_valid():
                data = form.cleaned_data
                if 'delete' in data and data['delete']:
                    self.project.participants.remove(form.instance)

    def post(self, request, *args, **kwargs):
        if 'submit_action' in request.POST:
            if request.POST['submit_action'] == 'remove_members':
                self.process_members(request.POST)
                messages.add_message(self.request,
                                     messages.SUCCESS,
                                     _('Project membership requests'
                                       ' have been updated'))
            if request.POST['submit_action'] == 'update_request':
                self.process_requests(request.POST)
                messages.add_message(request,
                                     messages.SUCCESS,
                                     _('Project membership requests'
                                       ' have been updated'))
            response = redirect(self.get_success_url())
        else:
            response = super().post(request, *args, **kwargs)
        return response

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated


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
        return self.request.user.is_authenticated

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
        is_member = user.is_authenticated and self.project.has_member(user)

        if is_member:
            return super().handle_no_permission()
        else:
            return self.handle_no_membership()

    def handle_no_membership(self):
        membership_impossible = (
            not self.request.user.is_authenticated
            or self.project.is_draft
            or self.project.has_member(self.request.user)
        )

        if membership_impossible:
            return super().handle_no_permission()
        else:
            return redirect('memberships-request',
                            project_slug=self.project.slug)


class InviteDetailView(generic.DetailView):
    model = membership_models.Invite
    slug_field = 'token'
    slug_url_kwarg = 'invite_token'

    def dispatch(self, request, invite_token, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(
                'membership-invite-update',
                invite_token=invite_token
            )
        else:
            return super().dispatch(request, *args, **kwargs)


class InviteUpdateView(mixin.LoginRequiredMixin, generic.UpdateView):
    model = membership_models.Invite
    form_class = membership_forms.InviteForm
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
    model = membership_models.Request
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
        membership_models.Request.objects.request_membership(project, user)
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
