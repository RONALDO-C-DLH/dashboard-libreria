from django import forms
from .models import Libro, Autor, Categoria, Stock, Venta

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'precio']
        widgets = {'fecha_publicacion': forms.DateInput(attrs={'type': 'date'})}

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise forms.ValidationError('El precio debe ser positivo.')
        return precio

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'fecha_nacimiento']
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['libro', 'cantidad_actual', 'fecha_actualizacion']
        widgets = {'fecha_actualizacion': forms.DateInput(attrs={'type': 'date'})}

    def clean_cantidad_actual(self):
        c = self.cleaned_data['cantidad_actual']
        if c < 0:
            raise forms.ValidationError('La cantidad debe ser positiva.')
        return c

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['libro', 'cantidad_vendida', 'fecha_venta']
        widgets = {'fecha_venta': forms.DateInput(attrs={'type': 'date'})}

    def clean_cantidad_vendida(self):
        c = self.cleaned_data['cantidad_vendida']
        if c < 0:
            raise forms.ValidationError('La cantidad debe ser positiva.')
        return c
