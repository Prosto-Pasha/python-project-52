from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from task_manager.users.forms import SignUpForm, ChangeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    model = User  # Model name
    context_object_name = 'users'  # Template list name
    template_name = 'users/index.html'  # Template path


class UserCreateView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'users/create.html'  # Template path
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # form.instance.user = self.request.user
        messages.success(self.request, _('Account created successfully'))
        return super(UserCreateView, self).form_valid(form)


class UserUpdateView(View):

    def check_user(self, request, param_id):
        if not request.user.is_authenticated:
            messages.error(request, _(
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            ))
            return redirect('login')
        elif param_id != request.user.id:
            messages.error(request, _(
                'У вас нет прав для изменения другого пользователя.'
            ))
            return redirect('users_index')

    def get(self, request, *args, **kwargs):
        param_id = kwargs.get('id')
        self.check_user(request, param_id)
        form = SignUpForm(instance=request.user)
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': request.user.id}
        )

    def post(self, request, *args, **kwargs):
        param_id = kwargs.get('id')
        self.check_user(request, param_id)
        current_user = User.objects.get(id=request.user.id)
        form = ChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            changed_user = form.save(commit=False)
            changed_user.user = request.user
            changed_user.save()
            login(request, current_user)
            messages.success(request, _('Пользователь успешно изменён'))
            return redirect('users_index')
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_id': request.user.id}
        )


class UserDelete(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(User, id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
        })
