from django.urls import path
from . import views

urlpatterns = [
    path('vista-carrito', views.carrito, name='carrito'),
]