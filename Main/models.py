from django.db import models
from django.conf import settings
from django.utils import timezone

class Tags(models.Model):
    TagTitle = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    text = models.TextField()
    image = models.ImageField()
    datePublished = models.DateField()
    tag = models.ForeignKey('Tags',on_delete=models.CASCADE,)
# Create your models here.
