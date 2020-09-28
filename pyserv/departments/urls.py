from django.urls import path
from departments.views import index, get_department

urlpatterns = [
    path('', index, name='home'),
    path('department/<str:slug>', get_department, name='department')
]
