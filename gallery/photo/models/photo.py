from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to='gallery_photos',
        verbose_name='Фото'
    )
    signature = models.CharField(
        null=False,
        blank=False,
        max_length=500,
        verbose_name='Подпись'
    )
    author = models.ForeignKey(
        null=False,
        to=get_user_model(),
        related_name='photo',
        blank=False,
        verbose_name='Автор',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"{self.author} - {self.signature}"
