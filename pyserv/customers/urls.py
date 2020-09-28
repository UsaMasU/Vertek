from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='customers'),
    path('requests', index, name='requests'),
    path('customer/<str:slug>', get_department, name='customer')
]