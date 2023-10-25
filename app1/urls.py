from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Agrega esta línea para importar settings
from django.conf.urls.static import static  # Agrega esta línea para importar la función static
from django.contrib.auth import views  # Importa las vistas de autenticación

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('stockapp.urls')),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login' ),
    path('logout/', views.LogoutView.as_view(), name='logout')
    
]

# Agrega la configuración de archivos estáticos y multimedia solo si estás en modo de desarrollo.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
