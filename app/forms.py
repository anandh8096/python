from django import forms
from app.models import UserProfileInfo
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserProInfo(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio','profile_pic')