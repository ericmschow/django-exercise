from django.db import models
from django.conf import settings
import datetime
from django import forms
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.name)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField(max_length=50)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.question_text)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes= models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
