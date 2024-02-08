from django.shortcuts import render
from .models import ServiceOne, ServiceTwo, ServiceThree

# Create your views here.

def index_view(request):
    service_one = ServiceOne.objects.all()
    {'service_ones': service_one}

    # Check if there is at least one object in the queryset
    if service_one.exists():
        # Pass only the first object to the context
        context = {'service_one': service_one[0]}
    else:
        # Handle the case when there are no objects
        context = {'service_one': None}

    service_two = ServiceTwo.objects.all()
    {'service_two': service_two}

    service_three = ServiceThree.objects.all()
    {'service_three': service_three}

    return render(request, 'index.html', {'service_ones': service_one})

def farmer_view(request):

    return render(request, 'farmer-page.html')

def logistics_view(request):

    return render(request, 'logistics-page.html')

def waste_management_view(request):

    return render(request, 'waste-management.html')