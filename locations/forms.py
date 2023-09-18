from django import forms
from .models import Location, LocationImage

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address', 'accessible_for_handicapped']

class LocationImageForm(forms.ModelForm):
    class Meta:
        model = LocationImage
        fields = ['image']
