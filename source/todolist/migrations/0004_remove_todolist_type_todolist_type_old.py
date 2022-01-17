# Generated by Django 4.0.1 on 2022-01-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_aimtype_alter_statuschoice_status_obj_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='type',
        ),
        migrations.AddField(
            model_name='todolist',
            name='type_old',
            field=models.ManyToManyField(related_name='aims_old', through='todolist.AimType', to='todolist.TypeChoice', verbose_name='Тип'),
        ),
    ]
