from django.urls import path

from . import viewsets

app_name = "users"

urlpatterns = [
    path("users/", viewsets.UserCreateView.as_view(), name="create"),
]
