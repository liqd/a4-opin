from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.utils import functional
from django.utils.translation import ugettext as _
from django.views import generic
from rules.compat import access_mixins as mixins

from euth.memberships import forms as member_forms
from euth.memberships import models as member_models
from euth.projects import models as project_models
from euth.users import models as user_models

from . import forms


class DashboardProfileView(mixins.LoginRequiredMixin,
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


class DashboardProjectListView(mixins.LoginRequiredMixin, generic.ListView):
    model = project_models.Project
    template_name = 'euth_dashboard/project_list.html'

    def get_queryset(self):
        return self.model.objects.filter(
            organisation__initiators=self.request.user
        )

    def get_success_url(self):
        return reverse('dashboard-project-list')


class DashboardProjectUpdateView(mixins.LoginRequiredMixin,
                                 generic.UpdateView):
    model = project_models.Project
    form_class = forms.ProjectForm
    template_name = 'euth_dashboard/project_form.html'


class DashboardProjectInviteView(mixins.LoginRequiredMixin,
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
                       kwargs={'slug': self.project.slug})


class DashboardProjectUserView(mixins.LoginRequiredMixin,
                               SuccessMessageMixin,
                               generic.FormView):

    form_class = modelformset_factory(
        member_models.Request,
        member_forms.RequestModerationForm,
        extra=0)
    template_name = 'euth_dashboard/project_users.html'
    success_message = _("User request sucessfully updated")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        qs = member_models.Request.objects.order_by('created').filter(
            project__slug=self.kwargs['slug']
        )
        kwargs['queryset'] = qs
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = context['form']
        context['project'] = project_models.Project.objects.get(
            slug=self.kwargs['slug']
        )
        return context

    def form_valid(self, formset):
        for form in formset.forms:
            print(form.instance)
            print(form.instance.creator)
            if form.cleaned_data['action'] == 'accept':
                form.instance.accept()
            if form.cleaned_data['action'] == 'decline':
                form.instance.decline()
        return super().form_valid(formset)

    def get_success_url(self):
        return self.request.path
