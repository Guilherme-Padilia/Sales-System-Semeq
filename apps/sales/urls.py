from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.new_sale),  
    path('sales/create/', views.create_sale),
    path('sales/search-customers/', views.search_customer),
    path('sales/search-addresses/', views.search_address_by_cep),
    path('sales/history/', views.sales_history),
    path('sales/history/', views.sales_history),
    path('modules/', views.modules),
    path('', views.index),
]