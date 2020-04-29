from django.db import models
from django.conf import settings
import random

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

def randomPage():
    count_page = Page.objects.all().count()
    random_index = int(random.random()*count_page)
    if Page.objects.filter(pk = random_index).exists():
        page = Page.objects.get(pk = random_index)
        return page
    else:
        return None

def randomUnicalPage(User):
    Page_unikal = False
    while(not Page_unikal):
        random_page = randomPage()
        if random_page != None:
            Page_unikal = not settingUser.objects.get(User = User).history.filter(pk = random_page.pk ).exists()
            print("1: " + str(Page_unikal))
            Page_unikal = not Page.objects.get(pk = random_page.pk).favorite.filter(pk = User.pk).exists() 
            print("2: " + str(Page_unikal))

    page = random_page
    return page

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

class PageStatmant(models.Model):
    Pages = models.ForeignKey('Page', on_delete=models.CASCADE)
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.User.username +" - "+ self.Pages.title + ": " + str(PageStatmant.objects.filter(User = self.User).count()) 