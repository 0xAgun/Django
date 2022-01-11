import django_filters
from .models import *

class Filtersproduct(django_filters.FilterSet):
    class Meta:
        model = sell
        fields = '__all__'
