from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views import generic
from rules.compat import access_mixins as mixins

from euth.documents import phases as document_phases
from euth.ideas import phases as idea_phases
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
                                 SuccessMessageMixin,
                                 generic.UpdateView):
    model = project_models.Project
    form_class = forms.ProjectForm
    success_message = _("Project has been updated")
    template_name = 'euth_dashboard/project_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = _('Edit project')
        return context

    def get_success_url(self):
        return reverse('dashboard-project-list')


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
            if form.cleaned_data['action'] == 'accept':
                form.instance.accept()
            if form.cleaned_data['action'] == 'decline':
                form.instance.decline()
        return super().form_valid(formset)

    def get_success_url(self):
        return self.request.path


class DashboardOverviewView(
        mixins.LoginRequiredMixin,
        generic.TemplateView):
    template_name = "euth_dashboard/dashboard_overview.html"


class DashboardCreateOverviewView(
        mixins.LoginRequiredMixin,
        generic.TemplateView):
    template_name = "euth_dashboard/dashboard_create_overview.html"


class DashboardCreateIdeaCollectionView(
        mixins.LoginRequiredMixin,
        SuccessMessageMixin,
        generic.CreateView):

    model = project_models.Project
    form_class = forms.ProjectCreateMultiForm
    template_name = 'euth_dashboard/project_multi_form.html'
    success_message = _("Your project has been created")
    initial = {
        'phase': [
            {'type': idea_phases.CollectPhase().identifier},
            {'type': idea_phases.RatingPhase().identifier},
            {'type': idea_phases.CommentPhase().identifier},
        ]
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['phase_extras'] = 3
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = _("New project based on DEVELOP IDEAS")
        return context

    def get_success_url(self):
        return reverse('dashboard-project-list')


class DashboardCreateCommentingTextView(
        mixins.LoginRequiredMixin,
        SuccessMessageMixin,
        generic.CreateView):

    model = project_models.Project
    form_class = forms.ProjectCreateMultiForm
    template_name = 'euth_dashboard/project_multi_form.html'
    success_message = _("Your project has been created")
    initial = {
        'phase': [
            {'type': document_phases.CommentPhase().identifier},
        ]
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['phase_extras'] = 1
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = _("New project based on DISCUSS AN ISSUE")
        return context

    def get_success_url(self):
        return reverse('dashboard-project-list')
