from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import settingUser

class MyUser(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class settingsForm(forms.ModelForm):
    class Meta:
        model = settingUser
        fields = ['category', 'Site', 'Time_to_new_page']

   # def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['name'].widget.attrs.update({'class': 'special'})
    #    self.fields['comment'].widget.attrs.update(size='40')

