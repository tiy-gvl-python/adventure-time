from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    text = models.TextField()
    slug = AutoSlugField(populate_from='title')
    score = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag')
    timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return 'User: {}\nTitle: {}'.format(self.user.username, self.title)

    class Meta:
        ordering = ['-score']


class Answers(models.Model):
    user = models.ForeignKey('Profile')
    question = models.ForeignKey(Question)
    text = models.TextField()
    score = models.IntegerField(default=0)
    timestamp = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return '{}'.format(self.question.title)

class Tag(models.Model):
    tag = models.CharField(max_length=45) #length of longest english word
    timestamp = models.TimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return '{}'.format(self.tag)

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
    user = models.OneToOneField(User, primary_key=True)
    email = models.EmailField()
    points = models.IntegerField(default=0)
    timestamp = models.TimeField(auto_now_add=True)
    administrator = models.BooleanField(default=False)

    def __str__(self):
        return 'username: {}\npoints: {}'.format(self.user, self.points)

    class Meta:
        ordering = ['-points']


class Click(models.Model):
    question = models.ForeignKey(Question, null=True)
    answer = models.ForeignKey(Answers, null=True)
    profile = models.ForeignKey(Profile, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)