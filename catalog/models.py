from django.db import models


# Create your models here.
class Breed(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Owner(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    tel = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Diagnosis(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    specialization = models.CharField(max_length=20)
    cost_rub = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Medicine(models.Model):
    title = models.CharField(max_length=20)
    dosage = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title} {self.dosage}'


class Animal(models.Model):
    nickname = models.CharField(max_length=20)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    age_years = models.DecimalField(decimal_places=2, max_digits=4)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    drug = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
    date = models.DateField()

    def __str__(self):
        return self.nickname
