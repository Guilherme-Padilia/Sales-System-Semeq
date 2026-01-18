from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.new_sale),  
    path('sales/create/', views.create_sale),
    path('sales/search-customers/', views.search_customer),
    path('sales/search-addresses/', views.search_address_by_cep),
    path('history/', views.sales_history),
    path('history/sales/', views.get_sales),
    path('modules/', views.modules),
]
