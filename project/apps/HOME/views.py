from django.shortcuts import render
from .models import Cilindro

# Create your views here.
def index (request):
    return render (request, "HOME/index.html", {"buscar": "busca por codigo"})

def home (request):
    registro_cilindros = Cilindro.objects.all()
    