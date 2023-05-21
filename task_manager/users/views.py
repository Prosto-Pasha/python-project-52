from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from task_manager.users.forms import SignUpForm, ChangeForm

from django.http import HttpResponse


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
            username = request.POST["username"]
            password = request.POST["password1"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            messages.success(request, _('Account created successfully'))
            return redirect('users_index')
        return render(request, "users/create.html", {'form': form})


class UserUpdateView(View):

    def get(self, request, *args, **kwargs):
        request_id = request.user.id
        if not request.user.is_authenticated:
            messages.error(request, _(
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            ))
            return redirect('login')
        elif kwargs.get('id') != request_id:
            messages.error(request, _(
                'У вас нет прав для изменения другого пользователя.'
            ))
            return redirect('users_index')

            #return HttpResponse("User ID %s." % kwargs.get('id'))
            #return HttpResponse("User ID %s." % request.user.id)
        form = SignUpForm(instance=request.user)
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': request_id}
        )

    def post(self, request, *args, **kwargs):
        request_id = request.user.id
        if not request.user.is_authenticated:
            messages.error(request, _(
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            ))
            return redirect('login')
        elif kwargs.get('id') != request_id:
            messages.error(request, _(
                'У вас нет прав для изменения другого пользователя.'
            ))
            return redirect('users_index')
        current_user = User.objects.get(id=request_id)
        form = ChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            changed_user = form.save(commit=False)
            changed_user.user = request.user

            print(1, form.cleaned_data['password'])

            # changed_user.password = form.cleaned_data['password1']
            changed_user.save()
            login(request, current_user)
            messages.success(request, _('Пользователь успешно изменён'))
            return redirect(to='users_index')
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': request_id}
        )


class UserDelete(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(User, id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
        })
