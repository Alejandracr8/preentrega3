from django.urls import path
from . import views
from .views import index, home, crear_cilindro, crear_BodegaPrincipal, crear_BodegaProveedor, crear_cliente

app_name = 'HOME'

urlpatterns = [
    path('', views.index, name='index'),
    path('registro_de_cilindros/',home, name='registro'  ),
    path('crear/', crear_cilindro, name='Crear Cilindro'),
    path('BodegaP/', crear_BodegaPrincipal, name='crear Bodega'),
    path('BodegaPro/', crear_BodegaProveedor, name='crear Bodega Proveedor'),
    path('crear cliente/', crear_cliente, name='crear cliente')
   
]