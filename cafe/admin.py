from django.contrib import admin
from .models import Producto
from .models import Usuario

admin.site.register(Producto)

admin.site.register(Usuario)
