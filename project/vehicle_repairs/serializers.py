from rest_framework import serializers
from django.contrib.auth.models import User
from vehicle_repairs.models import BlogPost
from vehicle_repairs.models import Vehicle
from vehicle_repairs.models import Comment
from vehicle_repairs.models import BlogPostLike
from vehicle_repairs.models import Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BlogPostLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPostLike
        fields = '__all__'


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
