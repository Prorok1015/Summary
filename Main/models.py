from django.db import models
import wikipediaapi

class Categorys(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    CategoryName = models.TextField()
class Sites(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    SiteName = models.TextField()
class Page(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=60)
    url = models.ForeignKey('Sites', on_delete=models.CASCADE)
    text = models.TextField()   
    summary = models.CharField(max_length=180)
    tag = models.ForeignKey('Categorys',on_delete=models.CASCADE)

    


