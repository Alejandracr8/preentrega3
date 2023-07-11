from django.contrib import admin
from . import models
# Register your models here.
admin.site.site_title = "Cilindros Escogas"


admin.site.register(models.BodegaPrincipal)
admin.site.register(models.BodegaProveedor)
admin.site.register(models.Cliente)
admin.site.register(models.Cilindro)

