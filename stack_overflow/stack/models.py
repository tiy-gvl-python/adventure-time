from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    text = models.TextField()
    slug = models.SlugField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')
    answers = models.ManyToManyField('Answers', through='Count')
    timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return 'User: {}\nTitle: {}'.format(self.user.username, self.title)

class Answers(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    score = models.IntegerField(default=0)
    timestamp = models.TimeField(auto_now_add=True)


class Tag(models.Model):
    tag = models.CharField(max_length=45) #length of longest english word
    timestamp = models.TimeField(auto_now_add=True)


class Count(models.Model):
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answers)
    count = models.IntegerField()

    def __str__(self):
        return 'Count: {}'.format(self.count)

class Vote(models.Model):
    upvote = models.BooleanField()
    downvote = models.BooleanField()
    timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        if self.upvote == True:
            return 'Upvote'
        elif self.downvote == True:
            return 'Downvote'
        else:
            return 'No vote'


class Profile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    points = models.IntegerField(default=0)
    timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return 'username: {}\npoints: {}'.format(self.user, self.profile)