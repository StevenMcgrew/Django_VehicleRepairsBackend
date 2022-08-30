from vehicle_repairs.serializers import (UserSerializer, UserProfileSerializer,
                                         BlogPostSerializer, VehicleSerializer,
                                         CommentSerializer, BlogPostLikeSerializer,
                                         TagSerializer)
from django.contrib.auth.models import User
from vehicle_repairs.models import UserProfile, BlogPost, Vehicle, Comment, BlogPostLike, Tag
from vehicle_repairs.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, viewsets


def query_params_handler(view, model):
    params = view.request.query_params
    if 'ids' in params:
        ids = params.get('ids')
        ids = [int(x) for x in ids.split(',')]
        return model.objects.filter(pk__in=ids)
    if 'user-id' in params:
        user_id = params.get('user-id')
        return model.objects.filter(user=user_id)
    return model.objects.all()


class CRUD(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass


class CreateRead(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    pass


class CreateReadUpdate(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin, viewsets.GenericViewSet):
    pass


class CreateReadDelete(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class UserViewSet(CRUD):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(CRUD):
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
    filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        query_params_handler(self, Tag)


class VehicleViewSet(CreateRead):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(CreateReadUpdate):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogPostLikeViewSet(CreateReadDelete):
    queryset = BlogPostLike.objects.all()
    serializer_class = BlogPostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TagViewSet(CreateRead):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query_params_handler(self, Tag)
