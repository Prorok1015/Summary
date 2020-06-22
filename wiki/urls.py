from django.urls import path
from . import views
from .views import MyRegisterFormView

urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/register/', MyRegisterFormView.as_view(), name="register"),
    path('favorit/', views.favorit, name='favorit'),
    path('history/', views.history, name='history'),
    path('settings/', views.settingsView.as_view(), name='settings'),
    path('add_favorite/', views.ajax_favorite, name='addfavorite'),
    path('add_history/', views.ajax_history, name='addhistory'),
    path('cron_task/', views.cron_task, name='cron')
]