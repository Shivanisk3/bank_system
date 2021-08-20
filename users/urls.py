from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.details, name= 'customers'),
    path('record/', views.record, name= 'record'),
    path('transfer/', views.transfer, name= 'transfer'),
]