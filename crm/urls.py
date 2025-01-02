from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('deals/', views.deal_list, name='deal_list'),
    path('deals/add/', views.add_deal, name='add_deal'),
]