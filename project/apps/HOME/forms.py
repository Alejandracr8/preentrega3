from django import forms
from .models import Cilindro, BodegaProveedor, BodegaPrincipal, Cliente

class CilindroForm(forms.ModelForm):
    class Meta:
        model = Cilindro
        fields = ["codigo", "capacidad", ]

class BodegaProveedorForm(forms.ModelForm):
    class Meta:
        model = BodegaProveedor
        fields = ["nombre", "direccion","codigo_cilindro" ]

class BodegaPrincipalForm(forms.ModelForm):
    class Meta:
        model = BodegaPrincipal
        fields = ["nombre", "direccion","codigo_cilindro" ]

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "direccion","codigo_cilindro" ]

