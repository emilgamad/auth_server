from django.shortcuts import render
from django.utils import timezone

from django.http import JsonResponse
from .models import AccessToken

def generate_token(request):
    token = AccessToken.objects.create()
    return JsonResponse({'token': token.token})

def validate_token(request):
    token = request.GET.get('token')
    try:
        access_token = AccessToken.objects.get(token=token, currently_in_use=False)
        access_token.currently_in_use = True
        access_token.last_used_at = timezone.now()
        access_token.save()
        return JsonResponse({'valid': True})
    except AccessToken.DoesNotExist:
        return JsonResponse({'valid': False, 'error': 'Cannot find token'})
