from django_filters import rest_framework as filters

from worc.apps.core.models import Candidate


class CandidateFilterSet(filters.FilterSet):
    class Meta:
        model = Candidate
        fields = "__all__"
