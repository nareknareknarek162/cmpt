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
        "HOST": env("DB_HOST", cast=str),
        "PORT": "5432",
    }
}
