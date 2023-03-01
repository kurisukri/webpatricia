from django.db import models
from django.utils import timezone
from datetime import datetime
import pytz

my_datetime = datetime.now(pytz.timezone('UTC'))
my_datetime = my_datetime.replace(tzinfo=None)

# CAMBIAR DE ACORDE AL CASO

class Cliente(models.Model):
    rut = models.CharField(max_length=500)
    nombre = models.CharField(max_length=500)
    direccion = models.CharField(max_length=500)
    ciudad = models.CharField(max_length=500)
    nrocontacto = models.IntegerField()

    def __str__(self):
        return self.rut


class Articulos (models.Model):
    fecha_ingreso = models.DateTimeField(default=my_datetime)
    nombre_articulo = models.CharField(max_length=500)
    categoria = models.CharField(max_length=500)
    codigo_barra = models.IntegerField()
    estado_articulo = models.BooleanField()
    estado = models.CharField(max_length=500)
    persona_prestamo = models.CharField(max_length=500)
    stock_sede = models.IntegerField()
    observaciones = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.nombre_articulo
    

class SolicitudReserva (models.Model):
    fecha = models.DateTimeField(default=my_datetime)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateTimeField(default=my_datetime)
    fecha_llegada = models.DateTimeField(null=True)
    nombre = models. CharField(max_length=100)
    rut = models.CharField(max_length=10)
    telefono = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    asignatura = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    estado_reserva = models.BooleanField(default=False, verbose_name="ESTADO SOLICITUDES")
    nombre_equipo = models.CharField(max_length=200)
    codigo_equipo = models.CharField(max_length=100)
    cantidad_solicitada = models.IntegerField() 

    def _str_(self):
     return self.rut


