from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .filters import Filtersproduct


def home(request):
    return render(request, 'base/test.html')

def allpro(request):
    productss = product.objects.all()
    contex = {'products': productss}
    return render(request, 'base/allproduct.html', contex)

def addproduct(request):
    return HttpResponse("adding a new product")

def selling(request):
    myfilter = Filtersproduct()
    contex = {'filter': myfilter}
    return render(request, 'base/body.html', contex)

def login(request):
    return HttpResponse("login here")