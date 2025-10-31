import os

from config.settings.django import BASE_DIR

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s - %(levelname)-5s [%(name)s] request_id=%(request_id)s %(message)s"
        }
    },
    "filters": {"request_id": {"()": "request_id.logging.RequestIdFilter"}},
    "handlers": {
        "general_logs": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs/general_log.log"),
            "mode": "w",
            "level": "DEBUG",
        },
        "db_logs": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs/db_log.log"),
            "mode": "w",
            "level": "DEBUG",
        },
        "console": {
            "class": "rich.logging.RichHandler",
            "level": "DEBUG",
            "filters": ["request_id"],
        },
    },
    "loggers": {
        "django": {
            "handlers": ["general_logs", "console"],
            "level": "INFO",
            "propagate": True,
        },
        "django.db.backends": {
            "handlers": ["db_logs", "console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
