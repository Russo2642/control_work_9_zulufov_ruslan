from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар'
    )
    activity = models.CharField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name='Сфера деятельности'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
