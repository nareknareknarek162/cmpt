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
    comment_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата и время комментария"
    )

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
