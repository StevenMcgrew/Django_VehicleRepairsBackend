from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    repair_steps = models.JSONField()
    thumbnail = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', related_name='blogposts', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', related_name='blogposts', on_delete=models.PROTECT )
    tags = models.ManyToManyField('Tag', related_name='blogposts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

class Vehicle(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    engine = models.CharField(max_length=5)
    is_verified = models.BooleanField(default=False)


class Comment(models.Model):
    comment = models.TextField(max_length=2000)
    blog_post = models.ForeignKey('BlogPost', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BlogPostLike(models.Model):
    blog_post = models.ForeignKey('BlogPost', related_name='blogpostlikes', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='blogpostlikes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['blog_post', 'user']


class Tag(models.Model):
    tag = models.CharField(max_length=30, unique=True)
