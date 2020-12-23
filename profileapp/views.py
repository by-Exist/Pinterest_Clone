from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator

from .decorators import profile_ownership_required
from .forms import ProfileCreateForm
from .models import Profile


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreateForm
    template_name = "profileapp/create.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})


@method_decorator(profile_ownership_required, "get")
@method_decorator(profile_ownership_required, "post")
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreateForm
    template_name = "profileapp/update.html"

    def get_success_url(self) -> str:
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})