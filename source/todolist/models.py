from django.db import models

TYPE_CHOICES = [('task', 'Задача'), ('bug', 'Баг'), ('enhancement', 'Улучшение')]
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class StatusChoice(models.Model):
    status_obj = models.CharField(max_length=11, choices=STATUS_CHOICES, default='new', verbose_name='Статус')

    def __str__(self):
        return f"{self.status_obj}"


class TypeChoice(models.Model):
    type_obj = models.CharField(max_length=12, null=False, choices=TYPE_CHOICES, default='task',  verbose_name='Тип')

    def __str__(self):
        return f"{self.type_obj}"


class ToDoList(models.Model):
    aim = models.CharField(max_length=200, null=False, blank=False, verbose_name='Задача')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Подробное описание')
    type = models.ForeignKey('todolist.TypeChoice', on_delete=models.PROTECT, default='task', related_name='type', verbose_name='Тип')
    status = models.ForeignKey('todolist.StatusChoice', on_delete=models.PROTECT, default='new', related_name='status', verbose_name='Статус')
    create_date = models.DateTimeField(null=False, auto_now=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(null=False, auto_now=True, verbose_name='Дата редактировнаия')

    def __str__(self):
        return f"{self.aim}{self.description}{self.type}{self.status}"

    class Meta:
        db_table = 'ToDoList'
        verbose_name = 'Список дел'
        verbose_name_plural = 'Списки дел'
