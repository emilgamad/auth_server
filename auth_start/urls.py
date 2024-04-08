from django.urls import path
from .views import generate_token, validate_token, check_token

urlpatterns = [
    #path('generate-token/', generate_token, name='generate_token'),
    path('validate-token/', validate_token, name='validate_token'),
    path('check-token',validate_token, name='check_token')
]
