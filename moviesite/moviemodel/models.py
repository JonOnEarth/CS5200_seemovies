# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# movie table
class movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default=' ')
    description = models.CharField(max_length=200, default=' ')
    watchlink = models.CharField(max_length=50, default=' ')
    posterlink = models.CharField(max_length=500, default=' ')
    actor = models.ManyToManyField('actor')
    director = models.ManyToManyField('director')
    category = models.ManyToManyField('category')

    def __str__(self):
        return self.title


# actor table
class actor(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20,default=' ')
    lastname = models.CharField(max_length=20,default=' ')
    description = models.CharField(max_length=200,default=' ')

    def __str__(self):
        return self.firstname


# director table
class director(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20,default=' ')
    lastname = models.CharField(max_length=20,default=' ')
    description = models.CharField(max_length=200,default=' ')

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


# review table
class review(models.Model):
    content = models.CharField(max_length=200, default=' ')
    movie = models.ForeignKey('movie', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


# category table
class category(models.Model):
    name = models.CharField(max_length=20, default=' ')

    def __str__(self):
        return self.name


class create(models.Model):
    movie = models.ForeignKey('movie', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


