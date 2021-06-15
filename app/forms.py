from django import forms
from .models import Suscriptores, Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidators
from bootstrap_datepicker_plus import DatePickerInput

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidators(max_file_size=3)])
    class Meta:
        model = Producto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        widgets = {
            "fecha_fabricacion": DatePickerInput(format='%d/%m/%Y')
        }

class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1","password1"]

class SuscripcionForm(forms.ModelForm):

    class Meta:
        model = Suscriptores
        fields = '__all__'

