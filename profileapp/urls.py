from profileapp.views import ProfileCreateView, ProfileUpdateView
from django.urls.conf import path


app_name = "profileapp"

urlpatterns = [
    path("create/", ProfileCreateView.as_view(), name="create"),
    path("update/<int:pk>", ProfileUpdateView.as_view(), name="update"),
]