from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UsernameField


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")
        field_classes = {'username': UsernameField}

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not data:
            raise ValidationError('You must fill in this field')
        return data
