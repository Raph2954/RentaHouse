from django.shortcuts import render
from tenant.models import Tenant, Apartments, Location, RentPerMonth

def tenantview(request):
    obj = Tenant.objects.all
    return render(request, 'Decision/tenant.html', {'tenants':obj})

def Apartmentsview(request):
    obj = Apartments.objects.all
    return render(request, 'Decision/apartments.html', {'apartments':obj})

def Locationview(request):
    obj = Location.objects.all
    return render(request, 'Decision/location.html', {'locations':obj})

def Price_Rangeview(request):
    obj = RentPerMonth.objects.all
    return render(request, 'Decision/PriceRange.html', {'price_range':obj})
