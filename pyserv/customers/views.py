import os
import webbrowser

from django.shortcuts import render, get_object_or_404, redirect
from customers.models import Customer, CustomerPerson, CustomerRequest


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

def get_requests(request):
    requests = CustomerRequest.objects.all()
    template = 'customers/requests.html'
    context = {
        'object_list': requests,
    }
    print(requests)
    for req in requests:
        print([i for i in req.__dict__.keys() if isinstance(i, str)])
    return render(request, template, context)

def open_folder(request):
    folder_path = request.GET.get('folder')
    webbrowser.open(os.path.realpath(folder_path))
    return redirect('requests')