from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils import translation
from django.contrib.auth.models import User


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, 'categories/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_index')

        return render(request, 'categories/create.html', {'form': form})


class UserUpdate(View):

    def get(self, request, *args, **kwargs):
        user_obj = get_object_or_404(User, id=kwargs['id'])
        #return render(request, 'articles/article.html', context={
        #    'article': article,
        #})


class UserDelete(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
        })
