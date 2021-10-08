from django import forms
from django.contrib.auth.models import User
from .models import Users

class UsersFrom(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
