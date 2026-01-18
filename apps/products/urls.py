from django.urls import path
from . import views

urlpatterns = [
    path('products/search/', views.search_products), 
]
