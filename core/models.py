from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200, db_index=True)
    fecha_publicacion = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.nombre

class Stock(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad_actual = models.IntegerField()
    fecha_actualizacion = models.DateField()

    def __str__(self):
        return f"{self.libro.titulo} – {self.cantidad_actual}"

class Venta(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()
    fecha_venta = models.DateField()

    def __str__(self):
        return f"{self.libro.titulo} – {self.fecha_venta}"
