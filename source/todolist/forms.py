from django import forms
from django.core.exceptions import ValidationError

from todolist.models import StatusChoice, TypeChoice, ToDoList, Projects


# class ToDoListForm(forms.Form):
#     aim = forms.CharField(max_length=200, required=True, label='Задача')
#     description = forms.CharField(max_length=2000, required=False, label='Описание',
#                                   widget=forms.Textarea())
#     status = forms.ModelChoiceField(queryset=StatusChoice.objects.all(), label='Статус')
#     type = forms.ModelMultipleChoiceField(queryset=TypeChoice.objects.all(), required=False, label="Тип",
#                                           widget=forms.CheckboxSelectMultiple(attrs={'width': '30', 'height': '30'}))


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        exclude = ['project']
        widgets = {
            'type': forms.CheckboxSelectMultiple
        }
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     if cleaned_data['aim'] == cleaned_data['description']:
    #         raise ValidationError("Задача и описание не должны быть одинаковыми!")
    #     return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = []