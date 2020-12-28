from django.forms import ModelForm, fields
from .models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ["image", "title", "description"]
