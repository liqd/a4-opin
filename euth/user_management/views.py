import uuid
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings

from . import sanatize_next
from .forms import LoginForm, RegisterForm, ActivateForm
from .emails import send_registration


def login_user(request):
    form = LoginForm(request.POST or None)
    next_action = sanatize_next(request)
    status = None
    if request.method == 'POST':
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return HttpResponseRedirect(sanatize_next(request))
        else:
            status = 400
    return render(request,
                  'user_management/login.html',
                  {'form': form, 'next_action': next_action},
                  status=status)


def logout_user(request):
    logout(request)
    next_action = request.GET.get('next') or request.POST.get('next')
    if next_action:
        return HttpResponseRedirect(next_action)
    else:
        return render_to_response(
            'user_management/logout.html', context_instance=RequestContext(request))


def register_user(request):
    form = RegisterForm(request.POST or None)
    next_action = sanatize_next(request)
    status = None
    if request.method == 'POST':
        if form.is_valid():
            registration = form.register(request)
            registration.next_action = next_action
            registration.save()
            send_registration(request, registration)
            return render(request, 'user_management/register_done.html')
        else:
            status = 400
    return render(request,
                  'user_management/register.html',
                  {'form': form, 'next_action': next_action},
                  status=status)


def activate_user(request, token):
    token = uuid.UUID(token)
    form = ActivateForm(request.POST or None, initial={'token': str(token)})
    status = None
    if request.method == 'POST':
        if form.is_valid():
            user, registration = form.activate(request)
            user.save()
            registration.delete()

            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)

            return HttpResponseRedirect(registration.next_action)
        else:
            status = 400
    return render(request, 'user_management/activate.html', {'form': form}, status=status)
