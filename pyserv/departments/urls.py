from django.urls import path
from departments.views import index

urlpatterns = [
    path('', index),
]
