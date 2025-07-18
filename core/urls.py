from django.urls import path
from .views import (
    home,
    libro_list, libro_create, libro_update, libro_delete, libro_data,
    autor_list, autor_create, autor_update, autor_delete,
    categoria_list, categoria_create, categoria_update, categoria_delete,
    stock_list, stock_create, stock_update, stock_delete,
    venta_list, venta_create, venta_update, venta_delete,
    ventas_data,
    dashboard,
)

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),

    # Libro
    path('libros/', libro_list, name='libro_list'),
    path('libros/nuevo/', libro_create, name='libro_create'),
    path('libros/<int:pk>/editar/', libro_update, name='libro_update'),
    path('libros/<int:pk>/eliminar/', libro_delete, name='libro_delete'),
    path('api/libro_data/', libro_data, name='libro_data'),

    # Autor
    path('autores/', autor_list, name='autor_list'),
    path('autores/nuevo/', autor_create, name='autor_create'),
    path('autores/<int:pk>/editar/', autor_update, name='autor_update'),
    path('autores/<int:pk>/eliminar/', autor_delete, name='autor_delete'),

    # Categoria
    path('categorias/', categoria_list, name='categoria_list'),
    path('categorias/nuevo/', categoria_create, name='categoria_create'),
    path('categorias/<int:pk>/editar/', categoria_update, name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', categoria_delete, name='categoria_delete'),

    # Stock
    path('stocks/', stock_list, name='stock_list'),
    path('stocks/nuevo/', stock_create, name='stock_create'),
    path('stocks/<int:pk>/editar/', stock_update, name='stock_update'),
    path('stocks/<int:pk>/eliminar/', stock_delete, name='stock_delete'),

    # Venta
    path('ventas/', venta_list, name='venta_list'),
    path('ventas/nuevo/', venta_create, name='venta_create'),
    path('ventas/<int:pk>/editar/', venta_update, name='venta_update'),
    path('ventas/<int:pk>/eliminar/', venta_delete, name='venta_delete'),

    # API
    path('api/ventas_data/', ventas_data, name='ventas_data'),
]
