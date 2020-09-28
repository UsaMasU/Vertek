from departments.models import Department


def departments(request):
    return {"departments_menu": Department.objects.all()}
