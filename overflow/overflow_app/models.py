from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True)
    reputation = models.IntegerField(default=0)
    member = models.BooleanField(default=False)
    moderator = models.BooleanField(default=False)
    administrator = models.BooleanField(default=False)

    def __str__(self):
        return 'username: {}, reputation: {}'.format(self.user, self.reputation)
'''
    class Meta:
        verbose_name = 'id'
        verbose_name_plural = 'id'

    def __str__(self):
        return "{}".format(self.user)
        '''


class Question(models.Model):
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=50)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return 'username: {}'.format(self.user)


class Reply(models.Model):
    user = models.ForeignKey(UserProfile)
    body = models.TextField()
    thread = models.ForeignKey(Question)
    reply_rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'username: {}, reputation: {}'.format(self.user, self.reputation)

    class Meta:
        ordering = ["-timestamp"]