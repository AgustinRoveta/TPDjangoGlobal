from django.db import models


# Define las opciones para el campo 'origen'
ORIGEN_CHOICES = [
    ('NAC', 'Nacional'),
    ('IMP', 'Importado'),
]
class Categorias(models.Model):
#Correspondera a la clase categorias: Un producto tendra solo una categoria pero una categoria puede estar presente en muchos productos
#Existira una relacion de uno a muchos
    category_name=models.CharField(max_length=20)
    def __str__(self):
        return self.category_name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        
class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    categoria_fk = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, default=1)
    imagen = models.ImageField(upload_to='stockapp', null=True, blank=True)
    origen = models.CharField(max_length=3, choices=ORIGEN_CHOICES, default='NAC')  # Campo con 'choices'

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
