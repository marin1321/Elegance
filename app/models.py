from django.db import models


# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos", blank=True, null=True)

    def __str__(self):
        return self.nombre

opciones_consulta = [
    ["Consulta","Consulta"],
    ["Reclamo","Reclamo"],
    ["Sugerencia","Sugerencia"],
    ["Felitaciones","Felitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, null=True)
    tipo_consulta = models.CharField(max_length=14, choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Suscriptores(models.Model):
    email = models.EmailField(blank=True, null=True)
    



