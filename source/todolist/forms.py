from django import forms
from django.core.exceptions import ValidationError

from .models import ToDoList, Projects


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        exclude = ['project']
        widgets = {
            'type': forms.CheckboxSelectMultiple
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = []