# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(to='stack.Answers', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('count', models.IntegerField()),
                ('answer', models.ForeignKey(to='stack.Answers')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('points', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('administrator', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-points'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', editable=False)),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tag', models.CharField(max_length=45)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('upvote', models.BooleanField()),
                ('downvote', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='stack.Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='count',
            name='question',
            field=models.ForeignKey(to='stack.Question'),
        ),
        migrations.AddField(
            model_name='click',
            name='profile',
            field=models.ForeignKey(to='stack.Profile', null=True),
        ),
        migrations.AddField(
            model_name='click',
            name='question',
            field=models.ForeignKey(to='stack.Question', null=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(to='stack.Question'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(to='stack.Profile'),
        ),
    ]
