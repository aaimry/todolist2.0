# Generated by Django 4.0 on 2022-02-20 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0011_projects_user_alter_projects_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='todolist.projects', verbose_name='Проект'),
        ),
    ]
