from django import forms
from listproperty.models import Property
from django_countries.widgets import CountrySelectWidget


class PropertyForm(forms.ModelForm):
    property_name = forms.CharField(widget=forms.TextInput(), required=True,max_length=200)
    Address = forms.CharField(widget=forms.TextInput(), required=True,max_length=200)
    Unit = forms.CharField(widget=forms.TextInput(), required=True,max_length=200)
    Type = forms.CharField(widget=forms.TextInput(), required=True,max_length=200)
    Beds = forms.CharField(widget=forms.TextInput(), required=False,max_length=200)
    Baths = forms.CharField(widget=forms.TextInput(), required=False,max_length=200)
    SQFT = forms.CharField(widget=forms.TextInput(), required=False,max_length=200)
    Photo = forms.ImageField
    Available_from = forms.DateField(widget=forms.DateInput(format='%d/%m/%y'))

    class Meta:
        model = Property
        fields =['property_name', 'Address', 'Unit', 'Type', 'Beds', 'Baths', 'SQFT', 'Country', 'Photo', 'Available_from']
        widgets = {'Country':CountrySelectWidget()}