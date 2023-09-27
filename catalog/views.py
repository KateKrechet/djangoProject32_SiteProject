from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse


# Create your views here.

def index(req):
    numkino = Film.objects.all().count()
    numact = Actor.objects.all().count()
    numfree = Film.objects.filter(status__film=1).count()
    data = {'k1': numkino, 'k2': numact, 'k3': numfree}
    return render(req, 'index.html', context=data)


# def allkino(req):
#     return render(req,'index.html')

class KinoList(generic.ListView):
    model = Film

class KinoDetail(generic.DetailView):
    model = Film


# def info(req,id):
#     film = Film.objects.get(id=id)
#     return HttpResponse(film.title)