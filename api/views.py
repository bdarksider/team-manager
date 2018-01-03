from rest_framework import generics
from .serializers import TeamMemberSerializer
from .models import TeamMember

class CreateView(generics.ListCreateAPIView):
    """Create behaviour of rest api"""
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist"""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    lookup_field = 'user_id'
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

        # for partial updates
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)