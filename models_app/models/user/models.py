from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "M", "Мужской"
        FEMALE = "F", "Женский"

    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    gender = models.CharField(
        max_length=1,
        choices=Gender,
        blank=False,
        null=False,
        verbose_name="Пол",
    )

    avatar = models.ImageField(verbose_name="Фото профиля", blank=True, null=True)
    avatar_thumbnail = ImageSpecField(
        source="avatar",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
