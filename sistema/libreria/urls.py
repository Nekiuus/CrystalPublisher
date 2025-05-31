from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('libros/', views.listar_libros, name='listar_libros'),
	path('libros/crear/', views.crear_libro, name='crear_libro'),
	path('libros/editar/<int:id>/', views.editar_libro, name='editar_libro'),
	path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('libros/', views.listar_libros, name='listar_libros'),
    path('inicio/', views.inicio, name='inicio'),]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)