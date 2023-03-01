from rest_framework import serializers
from .models import Articulos, SolicitudReserva

class ArticulosSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Articulos
        fields = ['fecha_ingreso', 'nombre_articulo', 'categoria', 'codigo_barra', 'estado_articulo', 'estado', 'persona_prestamo','stock_sede','observaciones']
        #CAMBIAR

class SolicitudReservaSerializers(serializers.ModelSerializer):

    class Meta:
        model = SolicitudReserva
        fields= ['fecha', 'destino', 'fecha_salida', 'fecha_llegada', 'nombre', 'rut', 'telefono', 'carrera', 'asignatura', 'profesor','estado_reserva','nombre_equipo', 'codigo_equipo','cantidad_solicitada']
