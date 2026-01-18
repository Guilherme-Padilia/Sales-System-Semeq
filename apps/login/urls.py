from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_screen),
    path('signin/', views.signin),
    path('', views.index),
]