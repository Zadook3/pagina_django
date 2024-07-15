from django.urls import path
from . import views

urlpatterns = [
    path('vista-mantencion', views.mantencion, name='mantencion'),
]