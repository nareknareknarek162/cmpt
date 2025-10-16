from django.db import models


class User(models.Model):
    GENDERS = [("M", "Мужской"), ("F", "Женский")]
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
