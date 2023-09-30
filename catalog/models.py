from django.db import models
from django.urls import reverse


# Create your models here.
class Breed(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название породы')

    def __str__(self):
        return self.title


class Owner(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя хозяина')
    surname = models.CharField(max_length=20, verbose_name='Фамилия хозяина')
    tel = models.CharField(max_length=12, verbose_name='Телефон хозяина')

    def __str__(self):
        return f'{self.name} {self.surname}'


class Diagnosis(models.Model):
    title = models.CharField(max_length=20, verbose_name='Диагноз')

    def __str__(self):
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя доктора')
    surname = models.CharField(max_length=20, verbose_name='Фамилия доктора')
    specialization = models.CharField(max_length=20, verbose_name='Специализация')
    cost_rub = models.IntegerField(verbose_name='Стоимость приема')

    def __str__(self):
        return f'{self.name} {self.surname} {self.specialization}'


class Medicine(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название лекарства')
    dosage = models.CharField(max_length=20, verbose_name='Доза')

    def __str__(self):
        return f'{self.title} {self.dosage}'


class Animal(models.Model):
    nickname = models.CharField(max_length=20, verbose_name='Кличка животного')
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, verbose_name='Порода')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, verbose_name='Хозяин')
    age_years = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Возраст(лет)')
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True, verbose_name='Диагноз')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, verbose_name='Доктор')
    drug = models.ManyToManyField(Medicine, verbose_name='Лекарствa')
    date = models.DateField(verbose_name='Дата приема')

    def __str__(self):
        return self.nickname

    def display_med(self):
        res = ''
        for m in self.drug.all():
            res += m.title + ' ' + m.dosage + ''
        return res

    display_med.short_description = 'Лекарства'

    def get_absolute_url(self):
        return reverse('info', args=[self.id])
