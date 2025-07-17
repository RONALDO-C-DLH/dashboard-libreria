from django.contrib import admin
from .models import Libro, Autor, Categoria, Stock, Venta

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'precio', 'fecha_publicacion')
    search_fields = ('titulo',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nacionalidad')
    search_fields = ('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'libro', 'cantidad', 'fecha_actualizacion')
    list_filter = ('fecha_actualizacion',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'libro', 'fecha_venta', 'cantidad', 'total')
    list_filter = ('fecha_venta',)
