
from django.urls import path
from AppTransporte import views

urlpatterns = [
  
    path('inicio', views.inicio, name="Inicio"),
    path('pasajero', views.pasajero, name="Pasajero"),
    path('chofer', views.chofer, name="Chofer"),
    path('transporte', views.transporte, name="Transporte"),
    path('terminal', views.terminal, name="Terminal"),
    path('pasajeroFormulario', views.pasajeroFormulario),
    path('choferFormulario', views.choferFormulario),
    path('transporteFormulario', views.transporteFormulario),
    path('terminalFormulario', views.terminalFormulario),
]