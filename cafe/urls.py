from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Api/', views.api, name='Api'),
    path('login/', views.login, name='login'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('pagina3/', views.pagina3, name='pagina3'),
    
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),


]
