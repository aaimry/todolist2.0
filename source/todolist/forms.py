from django import forms
from todolist.models import StatusChoice, TypeChoice


class ToDoListForm(forms.Form):
    aim = forms.CharField(max_length=200, required=True, label='Задача')
    description = forms.CharField(max_length=2000, required=False, label='Описание',
                                  widget=forms.Textarea())
    type = forms.ModelChoiceField(queryset=TypeChoice.objects.all(), label='Тип')
    status = forms.ModelChoiceField(queryset=StatusChoice.objects.all(), label='Статус')
