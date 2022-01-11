from django import forms
from .models import sell, product

class Selling_product(forms.ModelForm):
    class Meta:
        model = sell
        fields = ['namess', 'sell_price', 'sell_quantity',]

        widget = {
            'namess': forms.TextInput(attrs={'class': 'form-control'}),
            'sell_price': forms.TextInput(attrs={'class': 'form-control'}),
            'sell_quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }