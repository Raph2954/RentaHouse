from django import forms
from django.contrib.auth.models import User
from tenant.models import Tenant


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ('First_Name', 'Last_Name')



