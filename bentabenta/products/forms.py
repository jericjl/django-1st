from django import forms
from .models import Products

class ProductCreateForm(forms.Form):
    name        = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField()

