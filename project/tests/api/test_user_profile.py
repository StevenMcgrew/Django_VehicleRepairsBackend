import pytest


pytestmark = pytest.mark.django_db

def test_create_user_profile(client_and_user):
    (client, user) = client_and_user
    payload = {
        'user': user.id
    }
    response = client.post('/userprofiles/', payload)
    assert response.data['user'] == payload['user']
