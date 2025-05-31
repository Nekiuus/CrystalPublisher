from django.contrib import admin
from .models import Libro 

class LibroAdmin(admin.ModelAdmin): 
    list_display = ('titulo', 'descripcion') 
    search_fields = ('titulo', 'descripcion') 
    
admin.site.register(Libro, LibroAdmin)
