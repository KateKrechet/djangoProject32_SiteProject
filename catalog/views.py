from django.shortcuts import render
from .models import *
from django.views import generic


# Create your views here.

def index(req):
    visits = Animal.objects.all().count()
    workers = Doctor.objects.all().count()
    clients = Animal.objects.values('nickname').distinct().count()
    data = {'k1': visits, 'k2': clients, 'k3': workers}
    return render(req, 'index.html', context=data)


class AnimalList(generic.ListView):
    model = Animal


class AnimalDetail(generic.DetailView):
    model = Animal
