from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    name        = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField()
    class Meta:
        model = Products
        fields =[
            'name',
            'description',
            'price',
            'summary'

        ]

