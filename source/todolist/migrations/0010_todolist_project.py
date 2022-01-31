# Generated by Django 4.0.1 on 2022-01-31 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='project', to='todolist.projects', verbose_name='Проект'),
        ),
    ]
