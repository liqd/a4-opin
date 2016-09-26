from allauth.account import views as account_views
from allauth.socialaccount import views as socialaccount_views
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.utils import functional
from django.utils.translation import ugettext as _
from django.views import generic
from rules.compat import access_mixins as mixins
from rules.contrib import views as rules_views

from euth.memberships import models as member_models
from euth.organisations import models as org_models
from euth.phases import models as phase_models
from euth.projects import models as project_models
from euth.users import models as user_models

from . import blueprints, forms


def dashboard(request):
    return redirect('dashboard-profile')


class DashboardBaseMixin(mixins.LoginRequiredMixin,
                         generic.base.ContextMixin,):

    @functional.cached_property
    def user_has_organisation(self):
        return bool(self.request.user.organisation_set.all())

    @functional.cached_property
    def organisation(self):
        if 'organisation_slug' in self.kwargs:
            slug = self.kwargs['organisation_slug']
            return get_object_or_404(org_models.Organisation, slug=slug)
        else:
            return self.request.user.organisation_set.first()

    @functional.cached_property
    def other_organisations_of_user(self):
        user = self.request.user
        return user.organisation_set.exclude(pk=self.organisation.pk)


class DashboardEmailView(DashboardBaseMixin, account_views.EmailView):
    pass


class DashboardAccountView(DashboardBaseMixin,
                           socialaccount_views.ConnectionsView):
    pass


class DashboardProfileView(DashboardBaseMixin,
                           SuccessMessageMixin,
                           generic.UpdateView):

    model = user_models.User
    template_name = "euth_dashboard/profile_detail.html"
    form_class = forms.ProfileForm
    success_message = _("Your profile was successfully updated.")

    def get_object(self):
        return get_object_or_404(user_models.User, pk=self.request.user.id)

    def get_success_url(self):
        return self.request.path


class DashboardOrganisationUpdateView(DashboardBaseMixin,
                                      rules_views.PermissionRequiredMixin,
                                      SuccessMessageMixin,
                                      generic.UpdateView):
    model = org_models.Organisation
    form_class = forms.OrganisationForm
    slug_url_kwarg = 'organisation_slug'
    template_name = 'euth_dashboard/organisation_form.html'
    success_message = _('Organisation successfully updated.')
    permission_required = 'euth_organisations.modify_organisation'

    def get_success_url(self):
        return self.request.path


class DashboardProjectListView(DashboardBaseMixin,
                               rules_views.PermissionRequiredMixin,
                               generic.ListView):
    model = project_models.Project
    template_name = 'euth_dashboard/project_list.html'
    permission_required = 'euth_organisations.modify_organisation'

    def get_queryset(self):
        return self.model.objects.filter(
            organisation=self.organisation
        )

    def get_permission_object(self):
        return self.organisation

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_success_url(self):
        return reverse('dashboard-project-list')


class DashboardBlueprintListView(DashboardBaseMixin,
                                 rules_views.PermissionRequiredMixin,
                                 generic.TemplateView):
    template_name = 'euth_dashboard/blueprint_list.html'
    blueprints = blueprints.blueprints
    permission_required = 'euth_organisations.initiate_project'


class DashboardProjectCreateView(DashboardBaseMixin,
                                 rules_views.PermissionRequiredMixin,
                                 SuccessMessageMixin,
                                 blueprints.BlueprintMixin,
                                 generic.CreateView):
    model = project_models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'euth_dashboard/project_form.html'
    success_message = _('Project succesfully created.')
    permission_required = 'euth_organisations.initiate_project'

    def get_permission_object(self):
        return self.organisation

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['blueprint'] = self.blueprint
        kwargs['organisation'] = self.organisation
        return kwargs

    def get_success_url(self):
        return reverse('dashboard-project-list',
                       kwargs={
                           'organisation_slug': self.organisation.slug,
                       })


class DashboardProjectUpdateView(DashboardBaseMixin,
                                 rules_views.PermissionRequiredMixin,
                                 SuccessMessageMixin,
                                 generic.UpdateView):
    model = project_models.Project
    form_class = forms.ProjectCompleteForm
    template_name = 'euth_dashboard/project_form.html'
    success_message = _('Project successfully updated.')
    permission_required = 'euth_organisations.initiate_project'

    def get_permission_object(self):
        return self.organisation

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_success_url(self):
            return reverse('dashboard-project-edit',
                           kwargs={
                               'organisation_slug': self.organisation.slug,
                               'slug': self.get_object().slug
                           })

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        qs = phase_models.Phase.objects.filter(module__project=self.object)
        kwargs['phases__queryset'] = qs
        return kwargs


class DashboardProjectInviteView(DashboardBaseMixin,
                                 rules_views.PermissionRequiredMixin,
                                 SuccessMessageMixin,
                                 generic.FormView):
    form_class = forms.ProjectInviteForm
    template_name = 'euth_dashboard/project_invites.html'
    success_message = _("Invitations successfully sent.")
    permission_required = 'euth_organisations.initiate_project'

    def get_permission_object(self):
        return self.organisation

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

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


class DashboardProjectUserView(DashboardBaseMixin,
                               rules_views.PermissionRequiredMixin,
                               SuccessMessageMixin,
                               generic.FormView):

    form_class = forms.ProjectUserForm
    template_name = 'euth_dashboard/project_users.html'
    success_message = _("User request successfully updated.")
    permission_required = 'euth_organisations.initiate_project'

    def get_permission_object(self):
        return self.organisation

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

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
