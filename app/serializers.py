from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.query import QuerySet
from .models import Marca, Producto
from rest_framework import serializers

class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


class ProductoSerializers(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
    marca = MarcaSerializers(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="marca")
    nombre = serializers.CharField(required=True, min_length=2)

    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError(f"El productor {value} ya existe")
        else:
            return value


    class Meta:
        model = Producto
        fields = '__all__'