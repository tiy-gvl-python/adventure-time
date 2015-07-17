from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Question(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=30)
    text = models.TextField()


class Answers(models.Model):
    pass


class Vote(models.Model):
    pass


class Profile(models.Model):
    pass

