from articleapp.models import Article
from typing import Any, Dict
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django.views.generic.list import MultipleObjectMixin
from .decorators import account_ownership_required
from .forms import AccountUpdateForm


has_ownership = [account_ownership_required, login_required]


class AccountCreateView(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/create.html"


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = get_user_model()
    context_object_name = "target_user"
    template_name = "accountapp/detail.html"

    pagenate_by = 25

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        object_list = Article.objects.filter(writer=self.get_object())
        return super().get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountUpdateView(UpdateView):
    model = get_user_model()
    context_object_name = "target_user"
    form_class = AccountUpdateForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/update.html"


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountDeleteView(DeleteView):
    model = get_user_model()
    context_object_name = "target_user"
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/delete.html"
