from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Tenant(models.Model):
    First_Name = models.CharField(default='', max_length=100)
    Last_Name = models.CharField(default='', max_length=100)

    class Meta:
        verbose_name_plural = 'Tenants'

    def __str__(self):
        return self.First_Name


class TenantDecision(models.Model):
    Apartment_choice = models.ForeignKey('Apartments', on_delete=models.CASCADE)
    Location_of_Choice = models.ForeignKey('Location', on_delete=models.CASCADE)
    Price_Range = models.ForeignKey('RentPerMonth', on_delete=models.CASCADE)
    Country_of_choice = CountryField(default='')

    class Meta:
        verbose_name_plural = 'TenantDecisions'

    def __str__(self):
        return self.Apartment_choice


class Apartments(models.Model):
    type = models.CharField(default='', max_length=100)
    Description = models.CharField(default='None', max_length=250)
    Choice_of_Location = models.ForeignKey('Location', on_delete=models.CASCADE, default='None')

    class Meta:
        verbose_name_plural = 'Apartments'

    def __str__(self):
        return self.type


class Location(models.Model):
    State = models.CharField(default='None', max_length=100)
    LGA = models.CharField(default='None', max_length=100)
    District = models.CharField(default='None', max_length=100)

    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.State


class RentPerMonth(models.Model):
    range = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'PriceRangesPerMonth'

    def __str__(self):
        return self.range
