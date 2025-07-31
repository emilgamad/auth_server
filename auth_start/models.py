from django.db import models
from django.utils import timezone

class AccessToken(models.Model):
    """
    Model representing an access token for authentication.
    Fields:
        token: Unique token string.
        is_active: Whether the token is active.
        last_used_at: Last time the token was used.
        currently_in_use: Whether the token is currently in use.
        memo: Optional memo for the token.
    """
    token = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    last_used_at = models.DateTimeField(default=timezone.now)
    currently_in_use = models.BooleanField(default=False)
    memo = models.CharField(max_length=100, null=True)

    def __str__(self):
        """String representation of the AccessToken (returns the token string)."""
        return self.token