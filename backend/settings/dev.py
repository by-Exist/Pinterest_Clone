from .base import *
import environ

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# https://django-environ.readthedocs.io/en/latest/
env = environ.Env(
    # DJANGO_DEBUG 환경변수가 없을 때 기본값으로 False를 사용하도록 설정
    DJANGO_DEBUG=(bool, False),
)
environ.Env.read_env(".env")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    *MIDDLEWARE,
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}