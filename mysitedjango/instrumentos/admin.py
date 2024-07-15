from django.contrib import admin
from .models import TipoInstrumento, Instrumento, Compra, DetalleCompra



admin.site.register(TipoInstrumento)
admin.site.register(Instrumento)
admin.site.register(Compra)
admin.site.register(DetalleCompra)

# Register your models here.
