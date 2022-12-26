from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Person
# Create your views here.


def home(request):
    return HttpResponse("Home page aqua app")


class Add(CreateView):
    model = Person
    fields = ('name', 'age',)
    template_name = 'aqua/add.html'
    success_url = '/aqua/'
