from django.db import models


class Like(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="likes",
        related_query_name="like",
        verbose_name="Автор",
    )
    photo = models.ForeignKey(
        "Photo",
        on_delete=models.CASCADE,
        related_name="likes",
        related_query_name="like",
        verbose_name="Фото",
    )

    class Meta:
        db_table = "likes"
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
