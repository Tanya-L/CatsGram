# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone

class Person(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    telephon = models.IntegerField()
    address = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        abstract = True


class Breeder(Person):
    cattery = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.cattery)


class Owner(Person):
    pass


class Litter(models.Model):
    name = models.CharField(max_length=50)
    mother = models.ForeignKey("Cat", related_name="mother_litter", on_delete=models.CASCADE)
    father = models.ForeignKey("Cat", related_name="father_litter", on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField()

    breeder = models.ForeignKey(Breeder, on_delete=models.CASCADE)
    # notes   = models.TextField()

    def __str__(self):
        return self.name


class Cat(models.Model):

    # Mandatory fields
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    fur = models.CharField(max_length=50)

    # Optional
    age = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    # family = models.CharField(max_length=50, default="unknown")
    image = models.ImageField(blank=True, upload_to='cats')

    litter = models.ForeignKey(Litter, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name




# Create your polls models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= models.DateTimeField(default=timezone.now() - timedelta(days=1))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
