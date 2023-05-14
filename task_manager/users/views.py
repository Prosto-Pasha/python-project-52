from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from task_manager.users.forms import SignUpForm
from django.utils.translation import gettext_lazy as _


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Account created successfully'))
            return redirect('users_index')
        return render(request, "users/create.html", {'form': form})


class UserUpdate(View):

    def get(self, request, *args, **kwargs):
        pass
        # user_obj = get_object_or_404(User, id=kwargs['id'])
        # return render(request, 'articles/article.html', context={
        #    'article': article,
        # })


class UserDelete(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(User, id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
        })
