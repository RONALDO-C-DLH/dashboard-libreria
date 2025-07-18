from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count, Sum

from .models import Libro, Autor, Categoria, Stock, Venta
from .forms import (
    LibroForm, AutorForm, CategoriaForm, StockForm, VentaForm
)


# ----- List Views ------------------------------------------------------------
class BaseListView(ListView):
    paginate_by = 10
    def get_queryset(self):
        qs = super().get_queryset().order_by('id')
        q = self.request.GET.get('q')
        if q:
            field = 'titulo__icontains' if hasattr(self.model, 'titulo') else 'nombre__icontains'
            qs = qs.filter(**{field: q})
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class LibroListView(BaseListView):
    model = Libro
    template_name = 'libros/list.html'

class AutorListView(BaseListView):
    model = Autor
    template_name = 'autores/list.html'

class CategoriaListView(BaseListView):
    model = Categoria
    template_name = 'categorias/list.html'

class StockListView(BaseListView):
    model = Stock
    template_name = 'stocks/list.html'

class VentaListView(BaseListView):
    model = Venta
    template_name = 'ventas/list.html'

# ----- Create Views ---------------------------------------------------------
class BaseCreateView(CreateView):
    template_name_suffix = '/form'
    success_url = None

    def form_valid(self, form):
        messages.success(self.request, 'Registro creado correctamente')
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url

class LibroCreateView(BaseCreateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy('libro_list')

class AutorCreateView(BaseCreateView):
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy('autor_list')

class CategoriaCreateView(BaseCreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria_list')

class StockCreateView(BaseCreateView):
    model = Stock
    form_class = StockForm
    success_url = reverse_lazy('stock_list')

class VentaCreateView(BaseCreateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy('venta_list')

# ----- Update Views ---------------------------------------------------------
class BaseUpdateView(UpdateView):
    template_name_suffix = '/form'

    def form_valid(self, form):
        messages.success(self.request, 'Registro actualizado correctamente')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(f'{self.model._meta.model_name}_list')

class LibroUpdateView(BaseUpdateView):
    model = Libro
    form_class = LibroForm

class AutorUpdateView(BaseUpdateView):
    model = Autor
    form_class = AutorForm

class CategoriaUpdateView(BaseUpdateView):
    model = Categoria
    form_class = CategoriaForm

class StockUpdateView(BaseUpdateView):
    model = Stock
    form_class = StockForm

class VentaUpdateView(BaseUpdateView):
    model = Venta
    form_class = VentaForm

# ----- Delete Views ---------------------------------------------------------
class BaseDeleteView(DeleteView):
    template_name_suffix = '/confirm_delete'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Registro eliminado correctamente')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(f'{self.model._meta.model_name}_list')

class LibroDeleteView(BaseDeleteView):
    model = Libro

class AutorDeleteView(BaseDeleteView):
    model = Autor

class CategoriaDeleteView(BaseDeleteView):
    model = Categoria

class StockDeleteView(BaseDeleteView):
    model = Stock

class VentaDeleteView(BaseDeleteView):
    model = Venta

# ----- Dashboard Views ------------------------------------------------------
class DashboardLibroView(TemplateView):
    template_name = 'dashboard_libros.html'

    def get_data(self):
        qs = Libro.objects.values('fecha_publicacion').annotate(total=Count('id')).order_by('fecha_publicacion')
        return list(qs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data()
        context['total'] = Libro.objects.count()
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('ajax'):
            return JsonResponse(context['data'], safe=False)
        return super().render_to_response(context, **response_kwargs)

class DashboardAutorView(TemplateView):
    template_name = 'dashboard_autores.html'

    def get_data(self):
        qs = Autor.objects.values('fecha_nacimiento').annotate(total=Count('id')).order_by('fecha_nacimiento')
        return list(qs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data()
        context['total'] = Autor.objects.count()
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('ajax'):
            return JsonResponse(context['data'], safe=False)
        return super().render_to_response(context, **response_kwargs)

class DashboardCategoriaView(TemplateView):
    template_name = 'dashboard_categorias.html'

    def get_data(self):
        qs = Categoria.objects.values('nombre').annotate(total=Count('id'))
        return list(qs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data()
        context['total'] = Categoria.objects.count()
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('ajax'):
            return JsonResponse(context['data'], safe=False)
        return super().render_to_response(context, **response_kwargs)

class DashboardStockView(TemplateView):
    template_name = 'dashboard_stocks.html'

    def get_data(self):
        qs = Stock.objects.values('fecha_actualizacion').annotate(total=Sum('cantidad_actual')).order_by('fecha_actualizacion')
        return list(qs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data()
        context['total'] = Stock.objects.aggregate(total=Sum('cantidad_actual'))['total'] or 0
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('ajax'):
            return JsonResponse(context['data'], safe=False)
        return super().render_to_response(context, **response_kwargs)

class DashboardVentaView(TemplateView):
    template_name = 'dashboard_ventas.html'

    def get_data(self):
        qs = Venta.objects.values('fecha_venta').annotate(total=Sum('cantidad_vendida')).order_by('fecha_venta')
        return list(qs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data()
        context['total'] = Venta.objects.aggregate(total=Sum('cantidad_vendida'))['total'] or 0
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('ajax'):
            return JsonResponse(context['data'], safe=False)
        return super().render_to_response(context, **response_kwargs)

# ----- AJAX demo endpoints --------------------------------------------------
def ajax_insert_demo(request):
    """Insertar 5 libros y 5 ventas de ejemplo."""
    for i in range(5):
        libro = Libro.objects.create(
            titulo=f'Demo {timezone.now().timestamp()}-{i}',
            fecha_publicacion=timezone.now().date(),
            precio=10+i
        )
        Venta.objects.create(libro=libro, cantidad_vendida=1+i, fecha_venta=timezone.now().date())
    return JsonResponse({'status': 'ok'})

def ajax_update_demo(request):
    libros = Libro.objects.all()[:3]
    for l in libros:
        l.precio += 1
        l.save()
    ventas = Venta.objects.all()[:3]
    for v in ventas:
        v.cantidad_vendida += 1
        v.save()
    return JsonResponse({'status': 'ok'})

def ajax_delete_demo(request):
    ids = list(Libro.objects.values_list('id', flat=True).order_by('-id')[:2])
    Libro.objects.filter(id__in=ids).delete()
    return JsonResponse({'status': 'ok'})


def home(request):
    return DashboardLibroView.as_view()(request)
