from django.db import models


class Photo(models.Model):
    author = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="photos",
        related_query_name="photo",
        verbose_name="Автор",
    )
    description = models.CharField(
        blank=True, null=True, max_length=511, verbose_name="Описание"
    )
    publication_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата и время публикации"
    )
    image = models.ImageField(verbose_name="Фото")

    class Meta:
        db_table = "photos"
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
