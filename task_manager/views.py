from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_url = '/'
    success_message = _('Login successful')


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, _('You were successfully logout'))
    return redirect("/")
