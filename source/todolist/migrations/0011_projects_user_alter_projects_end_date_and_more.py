# Generated by Django 4.0 on 2022-02-16 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0010_todolist_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='user',
            field=models.ManyToManyField(related_name='user_project', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to='todolist.projects', verbose_name='Проект'),
        ),
    ]
