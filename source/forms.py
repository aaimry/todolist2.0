from django import forms
from todolist.models import STATUS_CHOICES


class ToDoListForm(forms.Form):
    aim = forms.CharField(max_length=200, required=True, label='Задача')
    deadline_at = forms.CharField(required=False, label='Дедлайн')
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Cтатус', initial=STATUS_CHOICES[0][1])
    description = forms.CharField(max_length=2000, required=False, label='Описание',
                                  widget=forms.Textarea())
