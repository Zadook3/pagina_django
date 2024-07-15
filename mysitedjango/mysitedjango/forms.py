from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from instrumentos.models import Instrumento, TipoInstrumento
from .validators import MaxSizeFileValidator
from django.forms import ValidationError


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User 
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

class InstrumentoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=15000000)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    tipo = forms.ModelChoiceField(queryset=TipoInstrumento.objects.all(), empty_label="Seleccionar")


    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Instrumento.objects.filter(nombre__iexact=nombre).exists() 

        if existe:
            raise ValidationError("Este nombre ya existe")
        
        return nombre
    

    class Meta:
        model = Instrumento
        fields = '__all__'

        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }