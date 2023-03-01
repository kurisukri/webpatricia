from django.urls import path, include
from .views import inicio, login, listadoarticulos, nuevoarticulo, modificararticulo, eliminararticulo, registrousuario, ArticulosViewSet, listadosolicitudes, modificarsolicitud, eliminarsolicitud, solicitarreserva, SolicitudReservaViewSet, ReportesExcel, SolicitudesExcel
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('articulos', ArticulosViewSet, SolicitudReservaViewSet)

urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('solicitarreserva/', solicitarreserva, name="solicitarreserva"),
    path('listadoarticulos/', listadoarticulos, name="listadoarticulos"),
    path('nuevoarticulo/', nuevoarticulo, name="nuevoarticulo"),
    path('modificararticulo/<id>/', modificararticulo , name="modificararticulo"),
    path('eliminararticulo/<id>/', eliminararticulo , name="eliminararticulo"),
    path('modificarsolicitud/<id>/', modificarsolicitud , name="modificarsolicitud"),
    path('eliminarsolicitud/<id>/', eliminarsolicitud , name="eliminarsolicitud"),
    path('registrousuario/', registrousuario , name="registrousuario"),
    path('api/', include(router.urls)),
    path('listadosolicitudes/', listadosolicitudes, name="listadosolicitudes"),
    path('reportearticulos/', views.ListArticulosPdf.as_view(), name="reportearticulos"),
    path('reportesolicitudes/', views.ListSolicitudesPdf.as_view(), name="reportesolicitudes"),
    path('reporte/', ReportesExcel, name="reporte"),
    path('solicitud_ex/', SolicitudesExcel, name="solicitud_ex"),


    



    
]