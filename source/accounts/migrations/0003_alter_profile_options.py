# Generated by Django 4.0 on 2022-02-22 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_create_profile_for_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('can_view_profiles', 'Может смотреть профили')], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
