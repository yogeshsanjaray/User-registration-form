from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserInfo

class Register_form(UserCreationForm):
    
    class Meta:    
        model = User                     
        fields = ("username","password1","password2")


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('name','email','phone')