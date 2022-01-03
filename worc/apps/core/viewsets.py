from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from worc.apps.core.filtersets import CandidateFilterSet
from worc.apps.core.models import Candidate
from worc.apps.core.serializers import CandidateSerializer


class CandidateListCreate(generics.ListCreateAPIView):
    """
    API endpoint that allows candidates to be viewed or edited.
    """

    permission_classes = [AllowAny]
    serializer_class = CandidateSerializer
    filterset_class = CandidateFilterSet
    queryset = Candidate.objects.order_by("-created_at")
