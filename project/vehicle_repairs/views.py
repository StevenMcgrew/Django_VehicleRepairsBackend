from vehicle_repairs.serializers import UserSerializer
from vehicle_repairs.serializers import BlogPostSerializer
from vehicle_repairs.serializers import VehicleSerializer

from django.contrib.auth.models import User
from vehicle_repairs.models import BlogPost
from vehicle_repairs.models import Vehicle

from vehicle_repairs.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets


# Automatically provides `list` and `retrieve` actions.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
