from django.shortcuts import render, redirect, get_object_or_404
from stockapp.forms import FormProducto
from stockapp.models import  Productos,Categorias
from django.contrib.auth.decorators import login_required


#Listar productos

def listarProductos(req):
    productos=Productos.objects.all() #SELECT * FROM productos
    categorias= Categorias.objects.all()#SELECT * FROM categorias
    formulario= FormProducto()
    contexto={"productos":productos, "categorias":categorias, "formulario":formulario}#el string es el tipo de nombre que le voy a dar para renderizarlo en el html, el any va a ser cualquier objeto que le quiera pasar, el objeto va a ser un diccionario 
    return render(req,'home.html',contexto)

#Eliminar un productos
@login_required
def eliminarProducto(req,id):
    producto=Productos.objects.get(id=id)
    producto.delete()
    return redirect('base')


#Editar productos
@login_required
def editarProducto(req,id):
    producto=get_object_or_404(Productos,id=id)
    if req.method=="GET":
        formulario= FormProducto(instance=producto)
        contexto={"producto": producto,"formulario": formulario}
        return render(req, 'editar.html', contexto)
    elif req.method =="POST":
        formulario=FormProducto(req.POST,req.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
        return redirect('base')

#Crear producto
@login_required
def crearProducto(req):
    form_producto=FormProducto(req.POST,req.FILES)
    if form_producto.is_valid():
        form_producto.save()
    return redirect('base')

