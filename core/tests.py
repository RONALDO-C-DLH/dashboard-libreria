from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date

from .models import Libro


class LibroModelTests(TestCase):
    def test_crear_libro_sin_titulo_lanza_validation_error(self):
        """Crear un Libro sin título debería lanzar ValidationError"""
        libro = Libro(titulo="", precio=10, fecha_publicacion=date.today())

        with self.assertRaises(ValidationError):
            libro.full_clean()
