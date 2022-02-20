from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile', verbose_name='Профиль')
    photo = models.ImageField(null=True, blank=True, upload_to='photos', verbose_name="Аватарка")
    githubLink = models.URLField(null=True, blank=True, max_length=200, verbose_name="Ссылка на GitHub")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="О себе")

    def __str__(self):
        return f'Профиль: {self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

