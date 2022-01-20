# Generated by Django 4.0.1 on 2022-01-17 12:00

from django.db import migrations


def transfer_tags(apps, schema_editor):
    ToDoList = apps.get_model('todolist.ToDoList')

    for aim_list in ToDoList.objects.all():
        aim_list.type.set(aim_list.type_old.all())


def rollback_transfer(apps, schema_editor):
    ToDoList = apps.get_model('todolist.ToDoList')

    for aim_list in ToDoList.objects.all():
        aim_list.type_old.set(aim_list.type.all())


class Migration(migrations.Migration):
    dependencies = [
        ('todolist', '0005_todolist_type'),
    ]

    operations = [
        migrations.RunPython(transfer_tags, rollback_transfer)
    ]