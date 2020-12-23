from articleapp.models import Article
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseForbidden


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs["pk"])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated