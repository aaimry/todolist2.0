# Generated by Django 4.0 on 2021-12-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aim', models.CharField(max_length=200, verbose_name='Задача')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=11, verbose_name='Статус')),
                ('deadline_at', models.DateField(blank=True, null=True, verbose_name='Дедлайн')),
            ],
        ),
    ]