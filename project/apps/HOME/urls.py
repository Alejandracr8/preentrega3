from django.urls import path
from . import views
from .views import index, home, crear_cilindro, crear_BodegaPrincipal, crear_BodegaProveedor, crear_cliente

app_name = 'HOME'

urlpatterns = [
    path('', views.index, name='index'),
    path('registro_de_cilindros/',home, name='registro'  ),
    path('crear/', crear_cilindro, name='crear_Cilindro'),
    path('BodegaP/', crear_BodegaPrincipal, name='crear_Bodega'),
    path('BodegaPro/', crear_BodegaProveedor, name='crear_Bodega_Proveedor'),
    path('crear_cliente/', crear_cliente, name='crear_cliente')
   
]