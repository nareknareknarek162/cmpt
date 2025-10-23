"""
Django settings for models_app.

"""

from config.settings.django import env

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", cast=str),
        "USER": env("DB_USER", cast=str),
        "PASSWORD": env("DB_PASSWORD", cast=str),
        "HOST": "localhost",
        "PORT": "5432",
    }
}
