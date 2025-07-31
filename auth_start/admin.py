from django.contrib import admin
from .models import AccessToken

@admin.register(AccessToken)
class AccessTokenAdmin(admin.ModelAdmin):
    """
    Admin interface for AccessToken model.
    Displays token, last used time, and usage status in the admin list view.
    """
    list_display = ('token', 'last_used_at', 'currently_in_use')