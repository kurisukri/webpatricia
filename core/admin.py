from django.contrib import admin
from .models import Cliente, Articulos, SolicitudReserva
# Register your models here.

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ['fecha_ingreso', 'nombre_articulo', 'categoria', 'codigo_barra', 'estado_articulo', 'estado', 'persona_prestamo','stock_sede','observaciones']
    search_fields = ['nombre_articulo']
    list_filter = ['nombre_articulo']
    list_per_page = 10

admin.site.register(Cliente)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(SolicitudReserva)