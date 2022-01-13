from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date
import datetime
from .models import *
from .forms import Selling_product, Adding_product


@login_required(login_url='login')
def home(request):
    today = date.today()
    dates = today.strftime("%B %d, %Y")
    recent = sell.objects.filter(sell_date=today)
    v = 0
    k = 0
    for x in recent:
        v += x.sell_price
    week = today - datetime.timedelta(days=6)
    weekly = sell.objects.filter(sell_date__range=[week, today])
    for weeks in weekly:
        k += weeks.sell_price


    contex = {'recent': recent, 'date': dates, 'total': v, 'week': k}
    return render(request, 'base/test.html', contex)

@login_required(login_url='login')
def allpro(request):
    productss = product.objects.all()
    contex = {'products': productss,}
    return render(request, 'base/allproduct.html', contex)

@login_required(login_url='login')
def addproduct(request):
        form = Adding_product(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addproduct')

        contex = {'form': form}
        return render(request, 'base/add.html', contex)

@login_required(login_url='login')
def selling(request):
    form = Selling_product()
    if request.method == 'POST':
        form = Selling_product(request.POST)
        if form.is_valid():
            instance = form.save()
            p = product.objects.get(id=instance.sell_name.id)
            p.stock -= instance.sell_quantity
            p.save()
            
            return redirect('sell')

    contex = {'form': form}
    return render(request, 'base/sell.html', contex)

def logins(request):
    if request.method == 'POST':
        lgusername = request.POST['loginusername']
        lgpassword = request.POST['loginpass']

        user = authenticate(username=lgusername, password=lgpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'Sucessfully logged in')
            return redirect('sell')
        else:
            messages.success(request, 'Sucessfully logged in')
            return redirect('login')


    return render(request, 'base/login.html')


def logoutmain(request):
    logout(request)
    messages.success(request, "successfully logged OUT")
    return redirect('login')

def searchs(request):
    query = request.GET['search']
    rub = product.objects.filter(name__icontains=query)
    contex = {'rab':rub}
    return render(request, 'base/search.html', contex)
    # return HttpResponse("search")
