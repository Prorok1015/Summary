from django.contrib import admin
from .models import Page,Sites,Categorys,settingUser

admin.site.register(settingUser)
admin.site.register(Categorys)
admin.site.register(Sites)
admin.site.register(Page)
# Register your models here.
