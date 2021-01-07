from django.urls import path
from .views import register, sign_in

urlpatterns = [
    path('register/', register, name='register'),
    path('sign_in/', sign_in, name='sign_in'),
]
