"""
URL configuration for ProyectoP_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from app_1.functions.dashboard import dashboard 
from app_1.functions.productos import productos
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login/', permanent=False), name='home'),
    path('login/', LoginView.as_view(template_name='inicio_sesion.html'),name='inicio_sesion'),
    path('logout/', LogoutView.as_view(),name='cerrar_sesion'),
    path('dashboard/', dashboard,name='dashboard'),
    path('productos/', productos,name='productos'),
    # path('productos/agregar_producto', agregar_producto,name='agregar_producto'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
