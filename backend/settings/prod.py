from .base import *

# TODO: 임시.
ALLOWED_HOSTS = [
    "*",
]

# TODO: 임시.
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}