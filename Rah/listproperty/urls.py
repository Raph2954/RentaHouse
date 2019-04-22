from django.urls import path
from listproperty import views


urlpatterns =[
    path('Property/', views.PropertyView, name='Property'),

]