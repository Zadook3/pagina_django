from django.urls import path
from . import views


urlpatterns = [
    path('vista-instrumentos-cuerda', views.instrumentos_cuerda, name='instrumentos_cuerda'),
    path('vista-instrumentos-percusion', views.instrumentos_percusion, name='instrumentos_percusion'),
    path('vista-audio', views.audio, name='audio'),

]