from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField("프로젝트 이미지", upload_to="project/")
    title = models.CharField("프로젝트 제목", max_length=20)
    description = models.CharField("설명", max_length=200, null=True)
    created_at = models.DateTimeField("생성일자", auto_now_add=True)

    def __str__(self):
        return self.title