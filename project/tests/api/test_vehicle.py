import pytest


pytestmark = pytest.mark.django_db

def test_create_vehicle(client_and_user):
    (client, user) = client_and_user
    payload = {
        'year': 2008,
        'make': 'Ford',
        'model': 'Taurus',
        'engine': '3.0L'
    }
    response = client.post('/vehicles/', payload)
    assert response.data['model'] == payload['model']
