from django.db import models
from multipleselectionfield import MultipleSelectionField
from django_countries.fields import CountryField


class Property(models.Model):
    bed_choices = (
        (1,1),(2,2),(3,3),(4,4),(5,'others')
    )
    bath_choices = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 'others')
    )
    type_choices = (
        (1, 'flat'),(2, 'bungalow'),(3, 'self-contain'),(4, 'studio apartment'),(5, 'single-room'),
    )
    property_name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Unit = models.CharField(max_length=200)
    Type = MultipleSelectionField(choices=type_choices, max_choices=1, null=True)
    beds = models.CharField(max_length=100, choices= bed_choices)
    Baths = models.CharField(max_length=100, choices= bath_choices)
    SQFT = models.CharField(max_length=50, default='None')
    Country = CountryField(default='')
    Photo = models.ImageField(width_field=300,height_field=300)
    Available_from = models.DateField(name=None)

    class Meta:
        verbose_name_plural = 'properties'

    def __str__(self):
        return self.property_name


class AddBeds(models.Model):
    number_of_beds = models.CharField(max_length=50, default='None')

    class Meta:
        verbose_name_plural = 'beds'

    def __str__(self):
        return self.number_of_beds
