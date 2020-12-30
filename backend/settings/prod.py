from .base import *

# TODO: django-envrion을 활용하여 bind(또는, 파일을 secret처럼 다루는 방식이 있나?)를 통해 여러 환경변수(비밀번호, DB 도메인 등등...)를 활용하는 방식이 더 적절하겠지만 우선 강좌대로 진행하자. 또한 Docker 스웜이나 컴포즈를 활용할 줄 알게 된다면 .env 파일을 사용하는 것이 아닌 다른 방식으로 구성하게 될 지도 모른다.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',

        # 환경변수들
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        
        # 같은 네트워크로 묶인 컨테이너의 Name.
        'HOST': 'postgres',
        'PORT': '5432',
    }
}