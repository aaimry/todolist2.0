# Generated by Django 4.0.1 on 2022-01-17 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todolist_options_alter_todolist_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AimType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='statuschoice',
            name='status_obj',
            field=models.CharField(max_length=30, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='type',
        ),
        migrations.AddField(
            model_name='todolist',
            name='type',
            field=models.ManyToManyField(related_name='aims', through='todolist.AimType', to='todolist.TypeChoice', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата редактировнаия'),
        ),
        migrations.AlterField(
            model_name='typechoice',
            name='type_obj',
            field=models.CharField(max_length=30, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='aimtype',
            name='aim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aim_type', to='todolist.todolist', verbose_name='Задача'),
        ),
        migrations.AddField(
            model_name='aimtype',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_aim', to='todolist.typechoice', verbose_name='Тип'),
        ),
    ]