from django.db import models
from django.utils import timezone

class AccessToken(models.Model):
    token = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    last_used_at = models.DateTimeField(default=timezone.now)
    currently_in_use = models.BooleanField(default=False)
    memo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.token