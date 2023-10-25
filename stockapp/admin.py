from django.contrib import admin

from stockapp.models import Productos,Categorias

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categorias)