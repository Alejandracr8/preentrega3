from django.shortcuts import render

# Create your views here.
def index (request):
    return render (request, "HOME/index.html", {"buscar": "busca por codigo"})