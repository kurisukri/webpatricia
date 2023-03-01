from django import forms
from django.forms import ModelForm
from .models import Articulos
from .models import SolicitudReserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

class ArticulosForm(ModelForm):

    class Meta:
        model = Articulos
        fields = ['fecha_ingreso' ,'nombre_articulo', 'categoria', 'codigo_barra', 'estado_articulo', 'estado', 'persona_prestamo','stock_sede','observaciones']

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2'] 

class SolicitudReservaForm(ModelForm):

    class Meta:
        model = SolicitudReserva
        fields= ['fecha', 'destino', 'fecha_salida', 'fecha_llegada', 'nombre', 'rut', 'telefono', 'carrera', 'asignatura', 'profesor','estado_reserva','nombre_equipo', 'codigo_equipo','cantidad_solicitada']

class SolicitudReservaConComboBoxForm(SolicitudReservaForm):
    # Obtén los nombres de los artículos del modelo Articulos
    opciones_articulos = [(a.nombre_articulo, a.nombre_articulo) for a in Articulos.objects.all()]

    # Agrega el campo del ComboBox al formulario
    nombre_articulo = forms.ChoiceField(choices=opciones_articulos)

