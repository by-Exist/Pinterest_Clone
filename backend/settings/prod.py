from .base import *

def read_secret(secret_name):
    with open(f"/run/secrets/{secret_name}") as f:
        secret = f.read().strip()

    return secret

# TODO: django-envrion을 활용하여 bind(또는, 파일을 secret처럼 다루는 방식이 있나?)를 통해 여러 환경변수(비밀번호, DB 도메인 등등...)를 활용하는 방식이 더 적절할 지, Docker secret을 활용하는 것이 더 적절할 지 잘 모르겠다.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = read_secret("DJANGO_SECRET_KEY")

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',

        # 환경변수들
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': read_secret("POSTGRES_PASSWORD"),
        
        # 같은 네트워크로 묶인 컨테이너의 Name.
        'HOST': 'postgres',
        'PORT': '5432',
    }
}