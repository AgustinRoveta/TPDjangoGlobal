from django import forms

from stockapp.models import Productos


class FormProducto(forms.ModelForm):
    class Meta:
        error= "Errors Found in your form"
        model = Productos
        fields= '__all__'
