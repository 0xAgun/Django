from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .filters import Filtersproduct
from .forms import Selling_product


def home(request):
    return render(request, 'base/test.html')

def allpro(request):
    productss = product.objects.all()
    contex = {'products': productss}
    return render(request, 'base/allproduct.html', contex)

def addproduct(request):
    return HttpResponse("adding a new product")

def selling(request):
    form = Selling_product(request.POST)
    if form.is_valid():
        form.save()
        return redirect('sell')

    contex = {'form': form}
    return render(request, 'base/addtest.html', contex)

def login(request):
    return HttpResponse("login here")