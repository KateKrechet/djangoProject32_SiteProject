from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
# импорт пользователей и групп, где они могут находиться
from django.contrib.auth.models import User, Group
from .form import Signupform


# Create your views here.

def index(req):
    numkino = Film.objects.all().count()
    numact = Actor.objects.all().count()
    numfree = Film.objects.filter(status__film=1).count()
    if req.user.username:
        username = req.user.first_name
        print(req.user.first_name, '#', req.user.id)
    else:
        username = 'Гость'
        print(req.user.id)
    print(req.user.username)
    data = {'k1': numkino, 'k2': numact, 'k3': numfree, 'username': username}
    # user = User.objects.create_user('user2', 'user2@mail.ru', 'useruser')
    # user.first_name = 'Vlad'
    # user.last_name = 'Petrov'
    # user.save()
    return render(req, 'index.html', context=data)


# def allkino(req):
#     return render(req,'index.html')

class KinoList(generic.ListView):
    model = Film
    paginate_by = 10


class KinoDetail(generic.DetailView):
    model = Film


class ActorList(generic.ListView):
    model = Actor
    paginate_by = 10


class ActorDetail(generic.DetailView):
    model = Actor


class DirectorList(generic.ListView):
    model = Director
    paginate_by = 10


class DirectorDetail(generic.DetailView):
    model = Director


# def info(req,id):
#     film = Film.objects.get(id=id)
#     return HttpResponse(film.title)

def status(req):
    k1 = Status.objects.all()
    data = {'podpiska': k1}
    return render(req, 'catalog/podpiska.html', data)


def prosmotr(req, id1, id2, id3):
    print(id1, id2, id3)
    mas = ['бесплатно', 'базовая', 'супер']  # film id2
    mas2 = ['free', 'based', 'super']  # user id3
    # id подписки в таблице
    if id3 == 0:
        status = 1
    else:
        status = User.objects.get(id=id3)
        status = status.groups.all()  # нашли список его подписок
        print(status)
        status = status[0].id  # нашли id его подписки, она одна
    print(status)

    if status >= id2:  # сравниваем статус человека и подписку фильма
        print('ok')
        permission = True
    else:
        print('нельзя')
        permission = False
    k1 = Film.objects.get(id=id1).title
    k2 = Group.objects.get(id=status).name
    k3 = Status.objects.get(id=id2).name
    data = {'kino': k1, 'status': k2, 'statuskino': k3, 'prava': permission}
    return render(req, 'prosmotr.html', context=data)


def buy(req, type):
    # находим номер текущего пользователя
    usid = req.user.id
    # находим его в таблице user
    user123 = User.objects.get(id=usid)
    # номер его подписки(группы)
    statusnow = user123.groups.all()[0].id
    # находим его подписку в таблицу group
    groupold = Group.objects.get(id=statusnow)
    # удаляем старую подписку user123
    groupold.user_set.remove(user123)
    # находим новую подписку в таблице group
    groupnew = Group.objects.get(id=type)
    # добавляем новую подписку
    groupnew.user_set.add(user123)
    k1 = groupnew.name
    data = {'podpiska': k1}
    return render(req, 'buy.html', data)


from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def registr(req):
    print(1)
    if req.POST:
        print(2)
        anketa = Signupform(req.POST)
        if anketa.is_valid():
            print(3)
            anketa.save()
            k1 = anketa.cleaned_data.get('username')
            k2 = anketa.cleaned_data.get('password')
            k3 = anketa.cleaned_data.get('first_name')
            k4 = anketa.cleaned_data.get('last_name')
            k5 = anketa.cleaned_data.get('email')
            user = authenticate(username=k1, password=k2) #сохраняет нового пользователя
            man = User.objects.get(username=k1) #найдем нового пользователя
            # заполним поля в таблице
            man.email = k5
            man.first_name = k3
            man.last_name = k4
            man.save()
            # входим на сайт
            # login(req, user)
            group = Group.objects.get(id=1) #находим бесплатную подписку
            # добавляем в подписку №1 созданного человека
            group.user_set.add(man)
            return redirect('home')
    else:
        anketa = Signupform()
    data = {'regform': anketa}
    return render(req, 'registration/registration.html', context=data)
