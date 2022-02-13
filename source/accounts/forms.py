from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UsernameField


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(max_length=100, required=True, label='First name')

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")
        field_classes = {'username': UsernameField}
