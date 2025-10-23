"""
Django settings for models_app.

"""
import os
import environ

from config.settings.settings import BASE_DIR

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

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

MEDIA_ROOT = os.path.join(BASE_DIR, "uploads/")
MEDIA_URL = "/uploads/"

AUTH_USER_MODEL = "models_app.User"
