from django import forms
from django.forms import ModelChoiceField


from stockapp.models import Categorias, Productos


class FormProducto(forms.ModelForm):
    nueva_categoria = forms.CharField(
        required=False, 
        label='Nueva Categoría', 
        widget=forms.TextInput(attrs={'placeholder': 'Escribe una nueva categoría'}))
    categoria_fk = forms.ModelChoiceField(
        queryset=Categorias.objects.all(),
        empty_label="Seleccionar categoría",
        required=False 
    )

    class Meta:
        model = Productos
        fields = '__all__'