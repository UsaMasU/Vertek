from django.shortcuts import render, get_object_or_404
from departments.models import Department, DepartmentPerson


def index(request):
    #department = get_object_or_404(Department, slug=slug)
    context = {
        'department_name': 'Under construction',
    }
    return render(request, 'departments/index.html', context)


def get_department(request, slug):
    department = get_object_or_404(Department, slug=slug)
    persons = DepartmentPerson.objects.filter(department=department.pk)
    context = {
        'department': department,
        'persons': persons,
    }
    return render(request, 'departments/department.html', context)