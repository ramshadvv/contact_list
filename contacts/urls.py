from django.urls import path
from .views import *

urlpatterns = [
    path('', contacts, name='list'),
    path('register', create_contacts ,name='register'),
]