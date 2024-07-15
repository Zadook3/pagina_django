from django.urls import path
from . import views

urlpatterns = [
    path('vista-sobrenosotros', views.sobrenosotros, name='sobrenosotros'),
]