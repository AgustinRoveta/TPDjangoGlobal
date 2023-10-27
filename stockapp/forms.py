from django import forms
from django.forms import ModelChoiceField


from stockapp.models import Categorias, Productos


class FormProducto(forms.ModelForm):
    class Meta:
        error= "Errors Found in your form"
        model = Productos
        fields= '__all__'
        categoria_fk = forms.ModelChoiceField(
        queryset=Categorias.objects.all(),
        empty_label="Seleccionar categoría")
