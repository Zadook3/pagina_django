from django.urls import path
from . import views

urlpatterns = [
    path('instrumentos-cuerda', views.instrumentos_cuerda, name='instrumentos_cuerda'),
    path('instrumentos-percusion', views.instrumentos_percusion, name='instrumentos_percusion'),
    path('audio', views.audio, name='audio'),
]