from platform import uname
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    Author = models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING)
    Creted_date = models.DateTimeField()
    Published_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
