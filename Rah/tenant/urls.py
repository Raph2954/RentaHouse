from django.urls import path
from tenant.views import tenantview, Apartmentsview, Locationview, Price_Rangeview
from tenant import views

urlpatterns=[
    path('tenant/', views.tenantview, name='tenant'),
    path('apartments/', views.Apartmentsview, name='apartments'),
    path('locations/', views.Locationview, name='locations'),
    path('price_range/', views.Price_Rangeview, name='price_range')
]