from django.shortcuts import render
from .models import ServiceOne, ServiceTwo, ServiceThree

# Create your views here.

def index_view(request):
    service_one = ServiceOne.objects.all()
    {'service_ones': service_one}

    service_two = ServiceTwo.objects.all()
    {'service_two': service_two}

    service_three = ServiceThree.objects.all()
    {'service_three': service_three}

    return render(request, 'index.html', {'service_ones': service_one})
