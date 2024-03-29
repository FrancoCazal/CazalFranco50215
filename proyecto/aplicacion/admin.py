from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Salada)
admin.site.register(Dulce)
admin.site.register(Bebida)
admin.site.register(Articulo)
admin.site.register(Avatar)