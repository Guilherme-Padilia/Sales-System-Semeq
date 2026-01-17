from django.urls import path
from .views import new_sale, modules, sales_history, index

urlpatterns = [
    path('sales/create/', new_sale),  
    path('sales/history/', sales_history),
    path('modules/', modules),
    path('', index),
]