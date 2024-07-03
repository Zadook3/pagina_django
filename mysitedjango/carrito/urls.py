from django.urls import path
from . import views

urlpatterns = [
    path('http://localhost:8000/carrito/vista-carrito', views.carrito, name='carrito'),
]