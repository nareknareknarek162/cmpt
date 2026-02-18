from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comment",
        verbose_name="Автор",
    )
    photo = models.ForeignKey(
        "Photo",
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comment",
        verbose_name="Фото",
    )
    text = models.CharField(
        blank=False, null=False, max_length=1023, verbose_name="Комментарий"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата и время создания", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата и время последнего обновления", auto_now=True
    )

    parent_comment = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name="Родительский комментарий",
    )

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
