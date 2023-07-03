from django.forms import ModelForm
from . models import *


class DistrictForm(ModelForm):
    class Meta:
        model=District
        fields='__all__'


class LocationForm(ModelForm):
    class Meta:
        model=Location
        fields='__all__'
        