from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('movie_list/',name='movies_list')
]
