from django import forms

from ..models import Photo, Residence


class ResidenceForm(forms.ModelForm):
    class Meta:
        model = Residence
        fields = ['title', 'description', 'price', 'street',
        'district', 'number', 'complement', 'is_published',
        'bathrooms', 'bedrooms', 
        ]