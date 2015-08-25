from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return 'username: {}, reputation: {}'.format(self.user, self.reputation)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=80)
    question = models.TextField()
    tag = models.ForeignKey(Tag, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} | {} | {}".format(self.title, self.timestamp, self.question, self.user)


class Answer(models.Model):
    user = models.ForeignKey(UserProfile)
    body = models.TextField()
    thread = models.ForeignKey(Question)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'username: {}'.format(self.user)

    class Meta:
        ordering = ["-timestamp"]
