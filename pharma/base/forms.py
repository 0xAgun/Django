from django import forms
from .models import sell, product

class Selling_product(forms.ModelForm):
    class Meta:
        model = sell
        fields = ['namess', 'sell_price', 'sell_quantity',]
        labels = {
            'namess': '',
            'sell_price': '',
            'sell_quantity': ''
        }


class Adding_product(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'amount', 'stock', 'price', 'category']
        labels = {
            'name': '',
            'amount': '',
            'stock': '',
            'price': '',
            'category': '',

        }