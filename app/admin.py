from django.contrib import admin
from .models import Contacto, Marca, Producto, Suscriptores
from .forms import ProductoForm

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre', 'precio', 'nuevo', 'marca']
    list_editable=['precio']
    search_fields=['nombre']
    list_filter=['nuevo', 'marca', 'precio']
    list_per_page=5
    form = ProductoForm
    

class SuscriptoresAdmin(admin.ModelAdmin):
    list_display=['email']

class ContactoAdmin(admin.ModelAdmin):
    list_per_page=10

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Suscriptores, SuscriptoresAdmin)