from rest_framework import serializers
from django.contrib.auth.models import User
from vehicle_repairs.models import BlogPost
from vehicle_repairs.models import Vehicle


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = BlogPost
        fields = ['url', 'id', 'title', 'repair_steps', 'thumbnail',
                  'is_published', 'user', 'vehicle']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blogposts = serializers.HyperlinkedRelatedField(many=True,
                                                     view_name='blogpost-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'blogposts']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Vehicle
        fields = ['url', 'id', 'year', 'make', 'model', 'engine', 'is_verified']


