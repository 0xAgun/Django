from django.urls import path
from .views import home, taskdetail

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('task/<int:pk>/', taskdetail.as_view(), name='task'), #pk means primary key (u can use anything beside task)

]