# Generated by Django 4.0 on 2021-12-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='description',
            field=models.CharField(blank=True, max_length=2000, verbose_name='Подробное описание'),
        ),
    ]