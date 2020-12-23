from django.db import models
from django.contrib.auth import get_user_model
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        verbose_name="게시물",
        on_delete=models.CASCADE,
        related_name="comment_set",
        blank=True,
    )
    writer = models.ForeignKey(
        get_user_model(),
        verbose_name="작성자",
        on_delete=models.CASCADE,
        related_name="comment_set",
        blank=True,
    )
    content = models.TextField("댓글 내용", max_length=511)
    created_at = models.DateTimeField(auto_now=True)