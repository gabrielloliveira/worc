from rest_framework import generics
from rest_framework.generics import get_object_or_404

from worc.apps.core.filtersets import CandidateFilterSet
from worc.apps.core.models import Candidate
from worc.apps.core.permissions import IsAdminOrReadOnly
from worc.apps.core.serializers import CandidateSerializer


class CandidateListCreate(generics.ListCreateAPIView):
    """
    API endpoint that allows candidates to be viewed or edited.
    """

    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CandidateSerializer
    filterset_class = CandidateFilterSet
    queryset = Candidate.objects.order_by("-created_at")


class CandidateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows candidates to be viewed, edited and deleted.
    """

    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.order_by("-created_at")

    def get_object(self):
        return get_object_or_404(Candidate, uuid=self.kwargs.get("uuid"))
