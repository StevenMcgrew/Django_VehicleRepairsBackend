from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    repair_steps = models.JSONField()
    thumbnail = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.PROTECT )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
