from django.urls import path
from .views import *

urlpatterns = [
    path('read', read_users),
    path('write', write_users),
]
