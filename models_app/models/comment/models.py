from django.db import models


class Comment(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    photo = models.ForeignKey("Photo", on_delete=models.CASCADE)
    text = models.TextField()
    comment_date = models.DateTimeField()

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
