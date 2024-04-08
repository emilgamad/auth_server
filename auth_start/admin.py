from django.contrib import admin
from .models import AccessToken

@admin.register(AccessToken)
class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'last_used_at', 'currently_in_use')