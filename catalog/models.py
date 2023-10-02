from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20, verbose_name='Жанр')

    def __str__(self):
        return self.name


class Director(models.Model):
    fname = models.CharField(max_length=20, verbose_name='Имя')
    lname = models.CharField(max_length=20, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Actor(models.Model):
    fname = models.CharField(max_length=20, verbose_name='Имя')
    lname = models.CharField(max_length=20, verbose_name='Фамилия')
    born = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
    country = models.CharField(max_length=20, verbose_name='Страна', blank=True, null=True)

    def __str__(self):
        return self.lname


class Status(models.Model):
    VIBOR = (('бесплатно', 'бесплатно'), ('базовая', 'базовая'), ('супер', 'супер'))
    name = models.CharField(max_length=20, choices=VIBOR, verbose_name='Подписка')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=20, verbose_name='Страна')

    def __str__(self):
        return self.name


class AgeRate(models.Model):
    choise = (('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'))
    rate = models.CharField(max_length=20, choices=choise, verbose_name='Рейтинг')

    def __str__(self):
        return self.rate


class Film(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default=1)
    rating = models.FloatField(verbose_name='Оценка')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, verbose_name='Режиссер')
    summary = models.TextField(max_length=500, verbose_name='Описание')
    year = models.IntegerField(verbose_name='Год')
    ager = models.ForeignKey(AgeRate, on_delete=models.SET_NULL, null=True)
    actor = models.ManyToManyField(Actor, verbose_name='Актеры')
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title

    def display_actors(self):
        res = ''
        for a in self.actor.all():
            res += a.lname + ' '
        return res

    display_actors.short_description = 'Актеры'

    def get_absolute_url(self):
        return reverse('info', args=[self.id,self.title])
        # return  f'kino/{self.id/{self.title}'
