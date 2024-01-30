from django import forms
from django.forms import ModelForm
from .models import Users

#CREATE USER FORM
class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email', 'phone')