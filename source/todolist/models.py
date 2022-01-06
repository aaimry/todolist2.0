from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class ToDoList(models.Model):
    aim = models.CharField(max_length=200, null=False, blank=False, verbose_name='Задача')
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Подробное описание')
    deadline_at = models.DateField(null=True, blank=True, verbose_name='Дедлайн')

    def __str__(self):
        return f"{self.aim} {self.status} {self.deadline_at}{self.description}"


class Meta:
    db_table = 'ToDoList'
    verbose_name = 'Список дел'
    verbose_name_plural = 'Список дел'