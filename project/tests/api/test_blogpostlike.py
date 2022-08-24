import pytest


pytestmark = pytest.mark.django_db

def test_create_blogpostlike(client_and_user, blogpost):
    (client, user) = client_and_user
    payload = {
        'blog_post': blogpost.id,
        'user': user.id
    }
    response = client.post('/blogpostlikes/', payload)
    assert response.data['blog_post'] == payload['blog_post']
