from django.db import models
from django.conf import settings
import wikipediaapi



class Categorys(models.Model):
    CategoryName = models.TextField()
    Status = models.BooleanField(default=False)

    def getCategory(self):
        return self.CategoryName

    def __str__(self):
        return self.CategoryName + " --- " + str(self.Status)

class Sites(models.Model):
    SiteName = models.TextField()

    def __str__(self):
        return self.SiteName
    
class Page(models.Model):   
    title = models.CharField(max_length=60)
    url = models.ForeignKey('Sites', on_delete=models.CASCADE)
    text = models.TextField()
    summary = models.CharField(max_length=180)
    tag = models.ForeignKey('Categorys',on_delete=models.CASCADE)
    favorite = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def  __str__(self):
        return self.title

class settingUser(models.Model):
    category = models.ForeignKey('Categorys', on_delete=models.CASCADE)
    Site = models.ForeignKey('Sites', on_delete=models.CASCADE)
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    history = models.ManyToManyField('Page')

    def __str__(self):
        return "settings: " + self.User.username 
