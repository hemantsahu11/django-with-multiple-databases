from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Practice
# Create your views here.


def home(request):
    return HttpResponse("Home page practice db App")


class Add(CreateView):
    model = Practice
    fields = ('title', 'content', 'app_name')
    template_name = 'practice_db/add.html'
    success_url = '/practice/'
