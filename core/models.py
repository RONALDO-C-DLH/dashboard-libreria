from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Stock(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_actualizacion = models.DateField()

    def __str__(self):
        return f"{self.libro.titulo} – {self.cantidad}"

class Venta(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.libro.titulo} – {self.fecha_venta}"
