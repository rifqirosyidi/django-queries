from django.db import models
from _datetime import date


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    date_created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=40)
    paradigm = models.CharField(max_length=20)
    date_created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
