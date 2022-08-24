import pytest


pytestmark = pytest.mark.django_db

def test_create_tag(client_and_user):
    (client, user) = client_and_user
    payload = {
        'tag': 'testing'
    }
    response = client.post('/tags/', payload)
    assert response.data['tag'] == payload['tag']
