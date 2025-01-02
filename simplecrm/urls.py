# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('crm.urls')),
# ]

# simplecrm/urls.py
from django.contrib import admin
from django.urls import path
from crm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('deals/', views.deal_list, name='deal_list'),
    path('deals/add/', views.add_deal, name='add_deal'),
]