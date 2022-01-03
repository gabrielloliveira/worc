from django.urls import path
from . import viewsets

app_name = "core"

urlpatterns = [
    path(
        "candidates/",
        viewsets.CandidateListCreate.as_view(),
        name="candidate_list_create",
    ),
]
