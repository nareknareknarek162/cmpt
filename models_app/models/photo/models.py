from django.db import models

from .fsm import Flow, State


class Photo(models.Model):
    author = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="photos",
        related_query_name="photo",
        verbose_name="Автор",
    )
    title = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="Название"
    )
    description = models.CharField(
        blank=True, null=True, max_length=511, verbose_name="Описание"
    )
    publication_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата и время публикации", auto_now=True
    )
    image = models.ImageField(verbose_name="Фото")

    state = models.CharField(
        max_length=63,
        default=State.ON_MODERATION,
        choices=State.choices,
        verbose_name="Статус",
    )

    def __str__(self):
        return self.title

    @property
    def flow(self):
        return Flow(self)

    class Meta:
        db_table = "photos"
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
