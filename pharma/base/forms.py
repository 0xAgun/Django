from django import forms
from .models import sell, product

class Selling_product(forms.ModelForm):
    class Meta:
        model = sell
        fields = ['sell_name', 'sell_price', 'sell_quantity', 'sell_cat']
        labels = {
            'sell_name': '',
            'sell_price': '',
            'sell_quantity': '',
            'sell_cat': ''
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