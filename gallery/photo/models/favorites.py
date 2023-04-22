from django.contrib.auth import get_user_model
from django.db import models

from photo.models import Photo


class Favorite(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='favorite_user',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    photo = models.ForeignKey(
        to=Photo,
        related_name='favorite_photo',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
