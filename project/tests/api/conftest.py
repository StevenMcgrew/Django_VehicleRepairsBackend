import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from vehicle_repairs.models import Vehicle, BlogPost


pytestmark = pytest.mark.django_db

@pytest.fixture
def client_and_user():
    client = APIClient()
    user = User.objects.create_user('user123', 'test@email.com', 'password123')
    client.force_authenticate(user=user)
    return (client, user)


@pytest.fixture
def vehicle():
    vehicle = Vehicle.objects.create(
        year=2008,
        make='Ford',
        model='Taurus',
        engine='3.0L',
    )
    return vehicle


@pytest.fixture
def blogpost(client_and_user, vehicle):
    (client, user) = client_and_user
    blogpost = BlogPost.objects.create(
        title='Some Title for Testing',
        repair_steps=[{ "text": "testing", "image": "test.jpg" }],
        thumbnail="thumbnail.jpg",
        user=user,
        vehicle=vehicle,
    )
    return blogpost
