"""
URL configuration for mysitedjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views 
from .views import agregar_instrumento, listar_instrumentos,\
     modificar_instrumento, eliminar_instrumento, registro
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
        path('', views.index, name='index'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('carrito/', include('carrito.urls')),
        path('instrumentos/', include('instrumentos.urls')),
        path('mantencion/', include('mantencion.urls')),
        path('sobrenosotros/', include('sobrenosotros.urls')),
        path('registro/', views.registro, name='registro'),
        path('agregar-instrumento/', agregar_instrumento, name="agregar_instrumento"),
        path('listar-instrumentos/', listar_instrumentos, name="listar_instrumentos"),
        path('modificar-instrumento/<id>/', modificar_instrumento, name="modificar_instrumento"),
        path('eliminar-instrumento/<id>/', eliminar_instrumento, name="eliminar_instrumento"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
