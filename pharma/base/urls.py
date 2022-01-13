from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sell/', views.selling, name='sell'),
    path('addproduct/', views.addproduct, name='addprod'),
    path('allproduct/', views.allpro, name='allprod'),
    path('login/', views.logins, name='login'),
    path('logout/', views.logoutmain, name='logout'),
    path('search/', views.searchs, name='search'),



]
