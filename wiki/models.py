from django.db import models
from django.conf import settings
from enum import Enum
import wikipediaapi



class Categorys(models.Model):
    CategoryName = models.TextField()
    Status = models.BooleanField(default=False)

    def getCategory(self):
        return self.CategoryName

    def __str__(self):
        return self.CategoryName

class Sites(models.Model):
    SiteName = models.TextField()

    def __str__(self):
        return self.SiteName
    
class Page(models.Model):   
    title = models.CharField(max_length=60)
    url = models.ForeignKey('Sites', on_delete=models.PROTECT)
    text = models.TextField()
    summary = models.CharField(max_length=180)
    tag = models.ForeignKey('Categorys',on_delete=models.PROTECT)
    favorite = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def existUser(self, username):
        return self.favorite.filter(username = username).exists()
         

    def  __str__(self):
        return self.title

class settingUser(models.Model):   
    One_hour = '1 '
    Two_hour = '2 '
    Six_hour = '3 '
    One_day  = '24'
    TO_TIME = [
        (One_hour, 'Каждый час'),
        (Two_hour, 'Каждые два часа'),
        (Six_hour, 'Каждые шесть часов'),
        (One_day, 'Каждый день'),
    ]
    category = models.ForeignKey('Categorys', on_delete=models.CASCADE)
    Site = models.ForeignKey('Sites', on_delete=models.CASCADE)
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Time_to_new_page = models.CharField(max_length=2, choices=TO_TIME, default=One_day)
    history = models.ManyToManyField('Page')

    def __str__(self):
        return "settings: " + self.User.username 
