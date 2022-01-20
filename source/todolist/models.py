from django.db import models

from todolist.validators import MinLengthValidator, MaxLengthValidator


class StatusChoice(models.Model):
    status_obj = models.CharField(max_length=30, verbose_name='Статус')

    def __str__(self):
        return f"{self.status_obj}"


class TypeChoice(models.Model):
    type_obj = models.CharField(max_length=30, verbose_name='Тип')

    def __str__(self):
        return f"{self.type_obj}"


class ToDoList(models.Model):
    aim = models.CharField(max_length=200, null=False, blank=False, verbose_name='Задача',
                           validators=(MaxLengthValidator(200), MinLengthValidator(5)))
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Подробное описание',
                                   validators=(MaxLengthValidator(2000), MinLengthValidator(5)))
    type = models.ManyToManyField('todolist.TypeChoice', related_name='aims', verbose_name='Тип')
    status = models.ForeignKey('todolist.StatusChoice', on_delete=models.PROTECT, default='new', related_name='status',
                               verbose_name='Статус')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата редактировнаия')

    def __str__(self):
        return f"{self.aim}{self.description}{self.type}{self.status}"

    class Meta:
        db_table = 'ToDoList'
        verbose_name = 'Список дел'
        verbose_name_plural = 'Списки дел'
