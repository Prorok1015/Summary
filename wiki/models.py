from django.db import models
import wikipediaapi

class Categorys(models.Model):
    CategoryName = models.TextField()
    Status = models.BooleanField(default=False)

    def getCategory(self):
        return self.CategoryName

class Sites(models.Model):
    SiteName = models.TextField()
class Page(models.Model):   
    title = models.CharField(max_length=60)
    url = models.ForeignKey('Sites', on_delete=models.CASCADE)
    text = models.TextField()   
    summary = models.CharField(max_length=180)
    tag = models.ForeignKey('Categorys',on_delete=models.CASCADE)
# Create your models here.
