from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return str(self.nombre)

class Usuario(models.Model):
    nombres = models.CharField(max_length=25)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    genero = models.CharField(max_length=1, choices=[('M', 'Hombre'), ('F', 'Mujer'), ('O', 'Otro')])
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombres

from django.db import models

class MiModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    campo3 = models.DateTimeField()

    def __str__(self):
        return self.campo1
