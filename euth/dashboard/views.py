from allauth.account import views as account_views
from allauth.socialaccount import views as socialaccount_views
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.utils import functional
from django.utils.translation import ugettext as _
from django.views import generic
from rules.compat import access_mixins as mixins
from rules.contrib import views as rules_views

from adhocracy4.phases import models as phase_models
from adhocracy4.projects import models as project_models
from euth.flashpoll import services
from euth.blueprintsuggest import mixins as blueprint_mixins
from euth.blueprintsuggest import blueprints
from euth.memberships import models as member_models
from euth.organisations import models as org_models
from euth.users import models as user_models

from . import emails, forms


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
        if self.organisation:
            return user.organisation_set.exclude(pk=self.organisation.pk)
        else:
            return None

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()


class DashboardEmailView(DashboardBaseMixin, account_views.EmailView):
    menu_item = 'email'


class DashboardAccountView(DashboardBaseMixin,
                           socialaccount_views.ConnectionsView):
    menu_item = 'connections'


class DashboardProfileView(DashboardBaseMixin,
                           SuccessMessageMixin,
                           generic.UpdateView):

    model = user_models.User
    template_name = "euth_dashboard/profile_detail.html"
    form_class = forms.ProfileForm
    success_message = _("Your profile was successfully updated.")
    menu_item = 'profile'

    def get_object(self):
        return get_object_or_404(user_models.User, pk=self.request.user.id)

    def get_success_url(self):
        return self.request.path


class ChangePasswordView(DashboardBaseMixin,
                         account_views.PasswordChangeView):
    menu_item = 'password'

    def get_success_url(self):
        return reverse('dashboard-password')


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
    menu_item = 'organisation'

    def get_success_url(self):
        return self.request.path


class DashboardProjectListView(DashboardBaseMixin,
                               rules_views.PermissionRequiredMixin,
                               generic.ListView):
    model = project_models.Project
    template_name = 'euth_dashboard/project_list.html'
    permission_required = 'euth_organisations.modify_organisation'
    menu_item = 'project'

    def get_queryset(self):
        return self.model.objects.filter(
            organisation=self.organisation
        )

    def get_permission_object(self):
        return self.organisation

    def get_success_url(self):
        return reverse('dashboard-project-list')


class DashboardBlueprintListView(DashboardBaseMixin,
                                 rules_views.PermissionRequiredMixin,
                                 generic.TemplateView):
    template_name = 'euth_dashboard/blueprint_list.html'
    blueprints = blueprints.blueprints
    permission_required = 'euth_organisations.initiate_project'
    menu_item = 'project'

    def get_permission_object(self):
        return self.organisation


class DashboardProjectCreateView(DashboardBaseMixin,
                                 rules_views.PermissionRequiredMixin,
                                 SuccessMessageMixin,
                                 blueprint_mixins.BlueprintMixin,
                                 generic.CreateView):
    model = project_models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'euth_dashboard/project_form.html'
    success_message = _('Project succesfully created.')
    permission_required = 'euth_organisations.initiate_project'
    menu_item = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = _("New project based on")
        context['module_settings'] = self.kwargs['module_settings']

        # initiating flashpoll data
        if context['module_settings'] == 'euth_flashpoll':
            context = services.fp_context_data_for_create_view(context, self)

        return context

    def get_permission_object(self):
        return self.organisation

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['blueprint'] = self.blueprint
        kwargs['organisation'] = self.organisation
        kwargs['creator'] = self.request.user

        if self.blueprint.settings_model:
            self.kwargs['module_settings'] = self.blueprint.settings_model[0]
        else:
            self.kwargs['module_settings'] = 'default'

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
    form_class = forms.ProjectUpdateForm
    template_name = 'euth_dashboard/project_form.html'
    success_message = _('Project successfully updated.')
    permission_required = 'euth_organisations.initiate_project'
    menu_item = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = _("Update project: " + self.object.name)
        # initiating flashpoll data
        if 'pollid' in self.kwargs:
            context = services.fp_context_data_for_update_view(context, self)

        return context

    def get_permission_object(self):
        return self.organisation

    def get_success_url(self):
        return reverse('dashboard-project-list',
                       kwargs={
                           'organisation_slug': self.organisation.slug,
                       })

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        qs = phase_models.Phase.objects.filter(module__project=self.object)
        kwargs['phases__queryset'] = qs

        if qs.first().type.startswith('euth_flashpoll'):
            settings_instance = qs.first().module.settings_instance
            kwargs['module_settings__instance'] = settings_instance
            self.kwargs['module_settings'] = 'euth_flashpoll'
            self.kwargs['pollid'] = settings_instance.key
        else:
            self.kwargs['module_settings'] = 'default'

        return kwargs


class DashboardProjectDeleteView(DashboardBaseMixin,
                                 rules_views.PermissionRequiredMixin,
                                 generic.DeleteView):
    model = project_models.Project
    form_class = forms.ProjectUpdateForm
    permission_required = 'euth_organisations.initiate_project'
    success_message = _('Your project has been deleted.')
    menu_item = 'project'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def delete(self, *args, **kwargs):
        response = super().delete(*args, **kwargs)
        emails.ProjectDeletedEmail.send(
            self.object,
            action_user=self.request.user
        )
        success_message = self.success_message
        messages.success(self.request, success_message)
        return response

    def get_success_url(self):
        return reverse('dashboard-project-list',
                       kwargs={
                           'organisation_slug': self.organisation.slug
                       })


class DashboardProjectInviteView(DashboardBaseMixin,
                                 rules_views.PermissionRequiredMixin,
                                 SuccessMessageMixin,
                                 generic.FormView):
    form_class = forms.ProjectInviteForm
    template_name = 'euth_dashboard/project_invites.html'
    success_message = _("Invitations successfully sent.")
    permission_required = 'euth_organisations.initiate_project'
    menu_item = 'project'

    def get_permission_object(self):
        return self.organisation

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
        for email in emails:
            member_models.Invite.objects.invite(user, project, email)
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
    menu_item = 'project'

    def get_permission_object(self):
        return self.organisation

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
        kwargs['moderators__instance'] = self.project
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
