from django.contrib.auth import login
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from articleapp.models import Article
from typing import Any, Optional
from django import http
from django.views.generic import RedirectView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from projectapp.models import Project
from subscriptionapp.models import Subscription


class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> Optional[str]:
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:

        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscriptionapp/list.html'
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list