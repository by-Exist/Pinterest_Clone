from commentapp.forms import CommentCreationForm
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from articleapp.decorators import article_ownership_required
from django.views.generic.edit import DeleteView, FormMixin, UpdateView
from articleapp.forms import ArticleCreationForm
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from articleapp.models import Article
from django.views.generic import CreateView, DetailView
from django.shortcuts import render

# Create your views here.
@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = "articleapp/create.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("articleapp:detail", kwargs={"pk": self.object.pk})


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    template_name = "articleapp/detail.html"
    form_class = CommentCreationForm
    context_object_name = "target_article"


auth_decos = [login_required, article_ownership_required]


@method_decorator(auth_decos, "get")
@method_decorator(auth_decos, "post")
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = "articleapp/update.html"
    context_object_name = "target_article"

    def get_success_url(self) -> str:
        return reverse("articleapp:detail", kwargs={"pk": self.object.pk})


@method_decorator(auth_decos, "get")
@method_decorator(auth_decos, "post")
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = "target_article"
    template_name = "articleapp/delete.html"
    success_url = reverse_lazy("articleapp:list")


class ArticleListView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "articleapp/list.html"
    paginate_by = 5
    ordering = ["-created_at"]