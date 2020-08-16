from django.urls import path
from pyserv.departments.views import index

urlpatterns = [
    path('', index),
]
