import pytest


pytestmark = pytest.mark.django_db

def test_create_comment(client_and_user, blogpost):
    (client, user) = client_and_user
    payload = {
        'comment': 'A comment for testing',
        'blog_post': blogpost.id,
        'user': user.id
    }
    response = client.post('/comments/', payload)
    assert response.data['comment'] == payload['comment']
