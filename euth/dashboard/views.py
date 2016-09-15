from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.utils import functional
from django.utils.translation import ugettext as _
from django.views import generic
from rules.compat import access_mixins as mixins

from euth.memberships import models as member_models
from euth.organisations import models as org_models
from euth.projects import models as project_models
from euth.users import models as user_models

from . import forms


def dashboard(request):
    organisation = request.user.organisation_set.first()
    if organisation:
        return redirect('dashboard-profile-org',
                        organisation_slug=organisation.slug)
    else:
        return redirect('dashboard-profile')


class DashboardBaseMixins(mixins.LoginRequiredMixin,
                          generic.base.ContextMixin):

    @functional.cached_property
    def user_has_organisation(self):
        return bool(self.request.user.organisation_set.all())

    @functional.cached_property
    def organisation(self):
        slug = self.kwargs['organisation_slug']
        return get_object_or_404(org_models.Organisation, slug=slug)

    @functional.cached_property
    def other_organisations_of_user(self):
        user = self.request.user
        return user.organisation_set.exclude(pk=self.organisation.pk)


class DashboardProfileView(DashboardBaseMixins,
                           SuccessMessageMixin,
                           generic.UpdateView):

    model = user_models.User
    template_name = "euth_dashboard/profile_detail.html"
    form_class = forms.ProfileForm
    success_message = _("Your profile was successfully updated")

    def get_object(self):
        return get_object_or_404(user_models.User, pk=self.request.user.id)

    def get_success_url(self):
        return self.request.path


class DashboardProjectListView(DashboardBaseMixins,
                               mixins.LoginRequiredMixin,
                               generic.ListView):
    model = project_models.Project
    template_name = 'euth_dashboard/project_list.html'

    def get_queryset(self):
        return self.model.objects.filter(
            organisation=self.organisation
        )

    def get_success_url(self):
        return reverse('dashboard-project-list')


class DashboardProjectUpdateView(DashboardBaseMixins,
                                 generic.UpdateView):
    model = project_models.Project
    form_class = forms.ProjectForm
    template_name = 'euth_dashboard/project_form.html'


class DashboardProjectInviteView(DashboardBaseMixins,
                                 mixins.LoginRequiredMixin,
                                 SuccessMessageMixin,
                                 generic.FormView):
    form_class = forms.ProjectInviteForm
    template_name = 'euth_dashboard/project_invites.html'
    success_message = _("Invitations sucessfully sent")

    @functional.cached_property
    def project(self):
        return project_models.Project.objects.get(
            slug=self.kwargs['slug']
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['project'] = self.project
        return kwargs

    def form_valid(self, form):
        emails = form.cleaned_data['emails']
        user = self.request.user
        project = self.project
        for (name, address) in emails:
            member_models.Invite.objects.invite(user, project, address)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard-project-users',
                       kwargs={
                           'organisation_slug': self.organisation.slug,
                           'slug': self.project.slug
                       })


class DashboardProjectUserView(DashboardBaseMixins,
                               SuccessMessageMixin,
                               generic.FormView):

    form_class = forms.ProjectUserForm
    template_name = 'euth_dashboard/project_users.html'
    success_message = _("User request sucessfully updated")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        qs = member_models.Request.objects.order_by('created').filter(
            project__slug=self.kwargs['slug']
        )
        kwargs['requests__queryset'] = qs
        qs = member_models.Invite.objects.order_by('created').filter(
            project__slug=self.kwargs['slug']
        )
        kwargs['invites__queryset'] = qs
        qs = user_models.User.objects.order_by('email').filter(
            project_participant__slug=self.kwargs['slug']
        )
        kwargs['users__queryset'] = qs
        kwargs['project'] = self.project
        return kwargs

    @functional.cached_property
    def project(self):
        return project_models.Project.objects.get(
            slug=self.kwargs['slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
