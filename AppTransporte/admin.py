from django.contrib import admin

from AppTransporte.views import pasajero
from .models import *

# Register your models here.
admin.site.register(Pasajero)

admin.site.register(Chofer)

admin.site.register(Transporte)

admin.site.register(Terminal)
