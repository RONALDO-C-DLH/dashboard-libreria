from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Libros
    path('libros/', views.LibroListView.as_view(), name='libro_list'),
    path('libros/nuevo/', views.LibroCreateView.as_view(), name='libro_create'),
    path('libros/<int:pk>/editar/', views.LibroUpdateView.as_view(), name='libro_update'),
    path('libros/<int:pk>/eliminar/', views.LibroDeleteView.as_view(), name='libro_delete'),
    path('dashboard/libros/', views.DashboardLibroView.as_view(), name='dashboard_libros'),

    # Autores
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    path('autores/nuevo/', views.AutorCreateView.as_view(), name='autor_create'),
    path('autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor_update'),
    path('autores/<int:pk>/eliminar/', views.AutorDeleteView.as_view(), name='autor_delete'),
    path('dashboard/autores/', views.DashboardAutorView.as_view(), name='dashboard_autores'),

    # Categorias
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nuevo/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('dashboard/categorias/', views.DashboardCategoriaView.as_view(), name='dashboard_categorias'),

    # Stock
    path('stock/', views.StockListView.as_view(), name='stock_list'),
    path('stock/nuevo/', views.StockCreateView.as_view(), name='stock_create'),
    path('stock/<int:pk>/editar/', views.StockUpdateView.as_view(), name='stock_update'),
    path('stock/<int:pk>/eliminar/', views.StockDeleteView.as_view(), name='stock_delete'),
    path('dashboard/stock/', views.DashboardStockView.as_view(), name='dashboard_stock'),

    # Ventas
    path('ventas/', views.VentaListView.as_view(), name='venta_list'),
    path('ventas/nuevo/', views.VentaCreateView.as_view(), name='venta_create'),
    path('ventas/<int:pk>/editar/', views.VentaUpdateView.as_view(), name='venta_update'),
    path('ventas/<int:pk>/eliminar/', views.VentaDeleteView.as_view(), name='venta_delete'),
    path('dashboard/ventas/', views.DashboardVentaView.as_view(), name='dashboard_ventas'),

    # AJAX demo
    path('ajax/insert/', views.ajax_insert_demo, name='ajax_insert'),
    path('ajax/update/', views.ajax_update_demo, name='ajax_update'),
    path('ajax/delete/', views.ajax_delete_demo, name='ajax_delete'),
]
