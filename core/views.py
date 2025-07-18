from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from django import forms
from .models import Libro, Autor, Categoria, Stock, Venta


# ModelForm para Libro
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'precio', 'fecha_publicacion']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'})
        }

def home(request):
    # Cargar todos los registros
    libros     = Libro.objects.all()
    autores    = Autor.objects.all()
    categorias = Categoria.objects.all()
    stocks     = Stock.objects.select_related('libro').all()
    ventas     = Venta.objects.select_related('libro').all()

    # Datos para gráfico de stock por libro
    stock_qs = (
        Stock.objects
        .values('libro__titulo')
        .annotate(total_stock=Sum('cantidad'))
        .order_by('libro__titulo')
    )
    chart_titles = [item['libro__titulo'] for item in stock_qs]
    chart_totals = [item['total_stock']   for item in stock_qs]

    return render(request, 'home.html', {
        'libros':     libros,
        'autores':    autores,
        'categorias': categorias,
        'stocks':     stocks,
        'ventas':     ventas,
        'chart_titles': chart_titles,
        'chart_totals': chart_totals,
    })

def dashboard(request):
    """Simple view to render the sales dashboard."""
    return render(request, 'dashboard.html')

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libro_list.html', {'libros': libros})

def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'libro_form.html', {'form': form})

def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro_form.html', {'form': form})

def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 'libro_confirm_delete.html', {'libro': libro})

from django.http import JsonResponse

def libro_data(request):
    # Listado de libros
    libros = list(
        Libro.objects
        .values('id', 'titulo', 'precio', 'fecha_publicacion')
        .order_by('id')
    )
    # Stock total por libro (ID y cantidad)
    stock_qs = (
        Stock.objects
        .values('libro_id')
        .annotate(total_stock=Sum('cantidad'))
        .order_by('libro_id')
    )
    stock = [
        {'libro_id': item['libro_id'], 'total_stock': item['total_stock']}
        for item in stock_qs
    ]
    return JsonResponse({'libros': libros, 'stock': stock})

from django.shortcuts import render, redirect

from .models import Autor
from django.shortcuts import get_object_or_404
from django import forms

# ModelForm para Autor
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'nacionalidad']

# Listado de Autores
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'autor_list.html', {'autores': autores})

# Crear Autor
def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'autor_form.html', {'form': form})

# Editar Autor
def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autor_form.html', {'form': form})

# Eliminar Autor
def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')
    return render(request, 'autor_confirm_delete.html', {'autor': autor})
# ── CRUD para Categoria ───────────────────────────────────────────────────────

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria_list.html', {'categorias': categorias})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_form.html', {'form': form})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'categoria_confirm_delete.html', {'categoria': categoria})


# ── CRUD para Stock ──────────────────────────────────────────────────────────

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['libro', 'cantidad', 'fecha_actualizacion']
        widgets = {
            'fecha_actualizacion': forms.DateInput(attrs={'type': 'date'})
        }

def stock_list(request):
    stocks = Stock.objects.select_related('libro').all()
    return render(request, 'stock_list.html', {'stocks': stocks})

def stock_create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'stock_form.html', {'form': form})

def stock_update(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm(instance=stock)
    return render(request, 'stock_form.html', {'form': form})

def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock_list')
    return render(request, 'stock_confirm_delete.html', {'stock': stock})


# ── CRUD para Venta ──────────────────────────────────────────────────────────

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['libro', 'fecha_venta', 'cantidad', 'total']
        widgets = {
            'fecha_venta': forms.DateInput(attrs={'type': 'date'})
        }

def venta_list(request):
    ventas = Venta.objects.select_related('libro').all()
    return render(request, 'venta_list.html', {'ventas': ventas})

def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'venta_form.html', {'form': form})

def venta_update(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'venta_form.html', {'form': form})

def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('venta_list')
    return render(request, 'venta_confirm_delete.html', {'venta': venta})

# al final del archivo core/views.py
from django.http import JsonResponse
from django.db.models.functions import TruncDate

def ventas_data(request):
    qs = (
        Venta.objects
        .annotate(fecha=TruncDate('fecha_venta'))
        .values('fecha')
        .annotate(total=Sum('total'))
        .order_by('fecha')
    )
    data = {
        'fechas': [item['fecha'].isoformat() for item in qs],
        'totales': [float(item['total']) for item in qs],
    }
    return JsonResponse(data)

