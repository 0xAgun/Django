from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sell/', views.selling, name='sell'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('allproduct/', views.allpro, name='allpro'),
    path('login/', views.login, name='login'),

]
