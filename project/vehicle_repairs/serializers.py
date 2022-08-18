from rest_framework import serializers
from django.contrib.auth.models import User
from vehicle_repairs.models import BlogPost
from vehicle_repairs.models import Vehicle
from vehicle_repairs.models import Comment
from vehicle_repairs.models import BlogPostLike


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blogposts = serializers.HyperlinkedRelatedField(many=True,
                    view_name='blogpost-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'blogposts']


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = BlogPost
        fields = ['url', 'id', 'title', 'repair_steps', 'thumbnail',
                  'is_published', 'user', 'vehicle']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Vehicle
        fields = ['url', 'id', 'year', 'make', 'model', 'engine', 'is_verified']


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ['comment', 'user', 'blog_post']


class BlogPostLikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BlogPostLike
        fields = ['user', 'blog_post']
