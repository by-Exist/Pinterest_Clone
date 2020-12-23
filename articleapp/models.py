from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(
        get_user_model(),
        verbose_name="작성자",
        on_delete=models.CASCADE,
        related_name="article_set",
    )
    title = models.CharField("제목", max_length=200, null=True)
    image = models.ImageField("이미지", upload_to="article/%Y/%m/%d", null=False)
    content = models.TextField("본문", null=True)
    created_at = models.DateTimeField("작성 날짜", auto_now_add=True)