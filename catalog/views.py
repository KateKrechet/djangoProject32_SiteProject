from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def index(req):
    numkino = Film.objects.all().count()
    numact = Actor.objects.all().count()
    numfree = Film.objects.filter(status__film=1).count()
    # try:
    #     username = req.user.first_name
    # except:
    #     username = 'Guest'
    print(req.user.username)
    data = {'k1': numkino, 'k2': numact, 'k3': numfree}
    # user = User.objects.create_user('user2', 'user2@mail.ru', 'useruser')
    # user.first_name = 'Vlad'
    # user.last_name = 'Petrov'
    # user.save()
    return render(req, 'index.html', context=data)


# def allkino(req):
#     return render(req,'index.html')

class KinoList(generic.ListView):
    model = Film
    paginate_by = 2


class KinoDetail(generic.DetailView):
    model = Film

# def info(req,id):
#     film = Film.objects.get(id=id)
#     return HttpResponse(film.title)
