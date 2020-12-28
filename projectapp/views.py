from subscriptionapp.models import Subscription
from typing import Any, Dict
from articleapp.models import Article
from django.views.generic.list import MultipleObjectMixin
from projectapp.forms import ProjectCreationForm
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import Project
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "projectapp/create.html"

    def get_success_url(self) -> str:
        return reverse("projectapp:detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = "target_project"
    template_name = "projectapp/detail.html"

    paginate_by = 25

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None

        object_list = Article.objects.filter(project=self.get_object())
        return super().get_context_data(object_list=object_list, subscription=subscription, **kwargs)


class ProjectListView(ListView):
    model = Project
    context_object_name = "project_list"
    template_name = "projectapp/list.html"
    paginate_by = 25