from django import forms
from .models import Contacto

#definir un formulario en el modelo de contacto

class ContactoForm(forms.ModelForm):
    #clase interna que contiene la configuracion del formulario

    class Meta:
        model = Contacto
        fields = ['nombre','email','mensaje']
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'mensaje':forms.Textarea(attrs={'class': 'form-control'}),
        }