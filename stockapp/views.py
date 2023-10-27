from django.shortcuts import render, redirect, get_object_or_404
from stockapp.forms import FormProducto
from stockapp.models import Productos, Categorias
from django.contrib.auth.decorators import login_required

# Listar productos
def listarProductos(req):
    productos = Productos.objects.all()
    categorias = Categorias.objects.all()
    formulario = FormProducto()
    contexto = {"productos": productos, "categorias": categorias, "formulario": formulario}
    return render(req, 'home.html', contexto)

# Eliminar un producto
@login_required
def eliminarProducto(req, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('base')

# Editar productos
@login_required
def editarProducto(req, id):
    producto = get_object_or_404(Productos, id=id)
    if req.method == "GET":
        formulario = FormProducto(instance=producto)
        contexto = {"producto": producto, "formulario": formulario}
        return render(req, 'edit.html', contexto)
    elif req.method == "POST":
        formulario = FormProducto(req.POST, req.FILES, instance=producto)
        if formulario.is_valid():
            nueva_categoria = req.POST.get("nueva_categoria")
            if nueva_categoria:
                # Intentar obtener la categoría existente o crear una nueva
                categoria, created = Categorias.objects.get_or_create(category_name=nueva_categoria)
                formulario.instance.categoria_fk = categoria
            formulario.save()
        return redirect('base')

# Crear producto
@login_required
def crearProducto(req):
    categorias = Categorias.objects.all()
    if req.method == 'POST':
        form_producto = FormProducto(req.POST, req.FILES)
        if form_producto.is_valid():
            nueva_categoria = req.POST.get("nueva_categoria")
            if nueva_categoria:
                # Intentar obtener la categoría existente o crear una nueva
                categoria, created = Categorias.objects.get_or_create(category_name=nueva_categoria)
                form_producto.instance.categoria_fk = categoria
            form_producto.save()
        return redirect('base')
    else:
        form_producto = FormProducto()
        contexto = {'categorias': categorias, 'form_producto': form_producto}
    return render(req, 'home.html', contexto)