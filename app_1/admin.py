from django.contrib import admin
from app_1.models import *

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado', 'imagen','activo')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
    fields = ('nombre', 'descripcion', 'categoria', 'estado', 'imagen')
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Categorias)
# Register your models here.
