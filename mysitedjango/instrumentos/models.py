from django.db import models
from django.contrib.auth.models import User

class TipoInstrumento(models.Model):

  nombre = models.CharField(max_length=100, unique=True)

  descripcion = models.TextField(blank=True, null=True)



  def __str__(self):

    return self.nombre



class Instrumento(models.Model):

  nombre = models.CharField(max_length=100)

  marca = models.CharField(max_length=100, blank=True, null=True)

  modelo = models.CharField(max_length=100, blank=True, null=True)

 

  precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)

  tipo = models.ForeignKey(TipoInstrumento, on_delete=models.CASCADE)

  imagen = models.ImageField(upload_to="instrumentos", null=True)
  def __str__(self):
     return self.nombre



  def __str__(self):

    return f"{self.nombre} ({self.tipo.nombre})"

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra {self.id} - {self.usuario.username} - {self.fecha}"

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='detalles', on_delete=models.CASCADE)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.instrumento.nombre} (Compra {self.compra.id})"

# Create your models here.
