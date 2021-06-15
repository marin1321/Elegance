from django.db import router
from django.urls import path, include
from .views import error_facebook, preguntas, resgistro, eliminar_producto, modificar_producto, listar_productos,\
     agregar_producto, contacto, galeria, home, ProductoViewset, MarcaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('marcas', MarcaViewset)

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('preguntas_frecuentes', preguntas, name='preguntas'),
    path('agregar-producto', agregar_producto, name='agregar'),
    path('listar-productos', listar_productos, name='listar'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar'),
    path('registrar/', resgistro, name='registra'),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    path('error-facebook/', error_facebook, name='error_facebook')
]