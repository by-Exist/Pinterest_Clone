from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="profile"
    )
    image = models.ImageField("프로필 이미지", upload_to="profile/%Y/%m/%d/", null=True)
    nickname = models.CharField("닉네임", max_length=20, unique=True, null=False)
    message = models.CharField("자기소개", max_length=100, null=True)