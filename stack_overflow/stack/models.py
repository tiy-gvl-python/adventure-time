from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Question(models.Model):
    user = models.ForeignKey('Profile')
    title = models.CharField(max_length=140)
    text = models.TextField()
    slug = AutoSlugField(populate_from='title')
    score = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag')
    timestamp = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField('Vote')

    def __str__(self):
        return 'User: {}\nTitle: {}'.format(self.user.user.username, self.title)

    @property
    def upvote_count(self):
        upvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_question=True).filter(upvote=True)
        return upvotes.count()

    @property
    def downvote_count(self):
        downvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_question=True).filter(downvote=True)
        return downvotes.count()

    class Meta:
        ordering = ['-score']


class Answers(models.Model):
    user = models.ForeignKey('Profile')
    question = models.ForeignKey(Question)
    text = models.TextField()
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField('Vote')

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return '{}'.format(self.question.title)

    @property
    def upvote_count(self):
        upvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_answer=True).filter(upvote=True)
        return upvotes.count()

    @property
    def downvote_count(self):
        downvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_answer=True).filter(downvote=True)
        return downvotes.count()


class Tag(models.Model):
    tag = models.CharField(max_length=45) #length of longest english word
    timestamp = models.DateTimeField(auto_now_add=True)
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


class Vote(models.Model):                               # I plan on handling this by making
    votee_pk = models.IntegerField(default=-1)          # a function in my views.py that
    voter = models.ForeignKey('Profile', default=None)  # will take in **kwargs and will
    upvote = models.BooleanField(default=False)                      # be able to put into context data
    downvote = models.BooleanField(default=False)               # when completed == True vote is active
    completed = models.BooleanField(default=False)  # that function can then be turned
    timestamp = models.DateTimeField(auto_now_add=True)  # into two buttons labeled upvote and downvote
    is_question = models.BooleanField(default=False)  # votee_pk is the model being voted on
    is_answer = models.BooleanField(default=False)
    def __str__(self):                            # params will still need to be set based on the
        if self.upvote == True:                   # instance and possibly in the the template
            return 'Upvote'                       # using if statments and for loops
        elif self.downvote == True:
            return 'Downvote'
        else:
            return 'No vote'


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    email = models.EmailField()
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    administrator = models.BooleanField(default=False)

    def __str__(self):
        return 'username: {}\npoints: {}'.format(self.user, self.score)

    @property
    def upvote_count(self):
        upvotes = Vote.objects.filter(voter=self.user).filter(upvote=True)
        return upvotes.count()

    @property
    def downvote_count(self):
        downvotes = Vote.objects.filter(voter=self.user).filter(downvote=True)
        return downvotes.count()

    class Meta:
        ordering = ['-score']


class Click(models.Model):
    question = models.ForeignKey(Question, null=True)
    answer = models.ForeignKey(Answers, null=True)
    profile = models.ForeignKey(Profile, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)