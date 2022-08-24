import pytest


pytestmark = pytest.mark.django_db

def test_create_blogpost(client_and_user, vehicle):
    (client, user) = client_and_user
    payload = {
        "title": "Some Title for Testing",
        "repair_steps": [
            { "text": "Step 1: Do something", "image": "some_image_1.jpg" },
            { "text": "Step 2: Do something else", "image": "some_image_2.jpg" }
        ],
        "thumbnail": "thumbnail_image_1.jpg",
        "is_published": False,
        "user": user.id,
        "vehicle": vehicle.id,
        "tags": []
    }
    response = client.post('/blogposts/', payload)
    assert response.data['title'] == payload['title']
