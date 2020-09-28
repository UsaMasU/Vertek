from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'message': 'Under construction',
    }
    return render(request, 'offers/index.html', context)
