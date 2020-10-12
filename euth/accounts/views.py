from django.contrib.auth import mixins
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views import generic

from euth.users import models as user_models

from . import forms


def dashboard_default(request):
    return redirect('account-profile')


class AccountProfileView(mixins.LoginRequiredMixin,
                         SuccessMessageMixin,
                         generic.UpdateView):

    model = user_models.User
    template_name = 'euth_accounts/profile_form.html'
    form_class = forms.ProfileForm
    success_message = _('Your profile was successfully updated.')

    def get_object(self):
        return get_object_or_404(user_models.User, pk=self.request.user.id)

    def get_success_url(self):
        return self.request.path
