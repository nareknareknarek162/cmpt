from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата рождения"
    )
    gender = models.CharField(
        max_length=1,
        choices=[("M", "Мужской"), ("F", "Женский")],
        blank=False,
        null=False,
        verbose_name="Пол",
    )

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
