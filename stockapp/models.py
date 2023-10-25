from django.db import models

# Create your models here.
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
    """Modelo para crear los objetos Productos"""
    nombre = models.CharField(max_length=30, null=False)
    precio = models.FloatField()
    stock  = models.IntegerField(default=0)
    categoria_fk=models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True,default=1)#esta sera la foreign key que nos relaciona con la class categorias
    imagen = models.ImageField(upload_to = 'stockapp', null=True,blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        managed= True
        verbose_name='Producto'
        verbose_name_plural= 'Productos' 
    