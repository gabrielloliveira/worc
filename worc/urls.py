from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Worc API",
        default_version="v1",
        description="Resolução do teste técnico da Worc.",
        terms_of_service="",
        contact=openapi.Contact(email="gabrielloliveira097@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("admin/", admin.site.urls),
    path("api/", include("worc.apps.core.urls", namespace="core")),
]
