from vehicle_repairs.serializers import UserSerializer
from vehicle_repairs.serializers import UserProfileSerializer
from vehicle_repairs.serializers import BlogPostSerializer
from vehicle_repairs.serializers import VehicleSerializer
from vehicle_repairs.serializers import CommentSerializer
from vehicle_repairs.serializers import BlogPostLikeSerializer
from vehicle_repairs.serializers import TagSerializer

from django.contrib.auth.models import User
from vehicle_repairs.models import UserProfile
from vehicle_repairs.models import BlogPost
from vehicle_repairs.models import Vehicle
from vehicle_repairs.models import Comment
from vehicle_repairs.models import BlogPostLike
from vehicle_repairs.models import Tag

from vehicle_repairs.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets


class UserViewSet(viewsets.ReadOnlyModelViewSet):  # Provides `list` and `retrieve` actions.
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):  # Provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogPostLikeViewSet(viewsets.ModelViewSet):
    queryset = BlogPostLike.objects.all()
    serializer_class = BlogPostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
