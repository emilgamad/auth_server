from django.urls import path
from .views import generate_token, validate_token

urlpatterns = [
    #path('generate-token/', generate_token, name='generate_token'),
    path('validate-token/', validate_token, name='validate_token'),
]
