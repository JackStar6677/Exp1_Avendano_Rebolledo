from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=60)

    def __str__(self):
        return str(self.nombre)