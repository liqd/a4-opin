from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import LoginForm


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
