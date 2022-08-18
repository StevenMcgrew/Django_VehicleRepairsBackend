from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    repair_steps = models.JSONField()
    thumbnail = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', related_name='blogposts', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.PROTECT )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

class Vehicle(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    engine = models.CharField(max_length=5)
    is_verified = models.BooleanField(default=False)
