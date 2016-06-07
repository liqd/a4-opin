import uuid
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings

from .forms import LoginForm, RegisterForm, ActivateForm
from .emails import send_registration


def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    return HttpResponseRedirect(reverse('process-listing'))
    return render(request, 'user_management/login.html', {'form': form})


def logout_user(request):
    logout(request)
    next_step = request.POST.get('next') or request.GET.get('next')
    if next_step:
        return HttpResponseRedirect(next_step)
    else:
        return render_to_response(
            'user_management/logout.html', context_instance=RequestContext(request))


def register_user(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            registration = form.register(request)
            registration.save()
            send_registration(request, registration)
            return render(request, 'user_management/register_done.html')
    return render(request, 'user_management/register.html', {'form': form})


def activate_user(request, token):
    token = uuid.UUID(token)
    form = ActivateForm(request.POST or None, initial={'token': str(token)})
    if request.method == 'POST':
        if form.is_valid():
            user, registration = form.activate(request)
            user.save()
            registration.delete()

            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)

            if registration.nexts:
                return HttpResponseRedirect(registration.nexts)
            else:
                return HttpResponseRedirect(reverse('process-listing'))
    return render(request, 'user_management/activate.html', {'form': form})
