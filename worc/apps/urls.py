from django.urls import path, include

urlpatterns = [
    path("", include("worc.apps.core.urls", namespace="core")),
    path("", include("worc.apps.users.urls", namespace="users")),
]
