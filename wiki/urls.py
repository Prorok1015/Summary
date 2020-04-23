from django.urls import path
from . import views
from .views import MyRegisterFormView

urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/register/', MyRegisterFormView.as_view(), name="register"),
    path('favorit/', views.favorit, name='favorit'),
    path('history/', views.history, name='history'),
    path('settings/', views.settings, name='settings'),
]