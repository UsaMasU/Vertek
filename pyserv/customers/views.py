from django.shortcuts import render, get_object_or_404
from customers.models import Customer, CustomerPerson


def index(request):
    #department = get_object_or_404(Department, slug=slug)
    customers = Customer.objects.all()
    print(customers)
    context = {
        'customers': customers,
    }
    return render(request, 'customers/index.html', context)


def get_department(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    persons = CustomerPerson.objects.filter(customer=customer.pk)
    context = {
        'customer': customer,
        'persons': persons,
    }
    return render(request, 'customers/customer.html', context)