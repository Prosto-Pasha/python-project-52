from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils import translation


class IndexView(View):

    def get(self, request, *args, **kwargs):
        translation.activate("ru")
        return render(request, 'index.html')
