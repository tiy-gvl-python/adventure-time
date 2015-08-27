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
    applies = models. BooleanField(default=False)

    def tag_it(self):
        if self.applies == True:
            return "{}".format(self.name)


class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    question = models.TextField()
    reputation = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} | {} | {}".format(self.title, self.timestamp, self.question, self.user)

    class Meta:
        ordering = ["-timestamp"]


class Answer(models.Model):
    user = models.ForeignKey(User)
    answer = models.TextField()
    question = models.ForeignKey(Question)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}, {}'.format(self.user, self.answer, self.question)

    class Meta:
        ordering = ["-timestamp"]
