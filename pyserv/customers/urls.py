from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='customers'),
    path('requests', get_requests, name='requests'),
    path('request/<str:slug>', get_department, name='customer_request'),
    path('person/<str:slug>', get_department, name='customer_person'),
    path('folders/', open_folder, name='folders'),
    path('customer/<str:slug>', get_department, name='customer'),
]