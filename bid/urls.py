from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('programas/', include('apps.programas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]