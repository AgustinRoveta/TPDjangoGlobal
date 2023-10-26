from django.urls import path
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static
from django.contrib.auth import views
from stockapp.views import editarProducto, eliminarProducto, listarProductos, crearProducto 

urlpatterns = [
    path('', listarProductos, name="base"),
    path('eliminar/<id>', eliminarProducto, name="eliminar"),      
    path('editar/<id>', editarProducto, name="editar"),
    path('crear', crearProducto, name='crear'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
