from django.contrib.auth import get_user_model
from django.db import models
from projectapp.models import Project

# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'project')