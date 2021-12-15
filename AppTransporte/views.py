from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppTransporte.models import Chofer, Pasajero, Transporte, Terminal
from AppTransporte.forms import ChoferFormulario, PasajeroFormulario, TransporteFormulario, TerminalFormulario

def choferFormulario(request):
    
      if request.method == 'POST':

            miFormulario = ChoferFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  chofer = Chofer (nombre=informacion['nombre'], apellido=informacion['apellido'], numeroDeDocumento=informacion['numeroDeDocumento'], numeroDeLicencia=informacion['numeroDeLicencia']) 

                  chofer.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ChoferFormulario() #Formulario vacio para construir el html

      return render(request, "AppTransporte/choferFormulario.html", {"miFormulario":miFormulario})
  
def pasajeroFormulario(request):
        
      if request.method == 'POST':

            miFormulario = PasajeroFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  pasajero = Pasajero (nombre=informacion['nombre'], apellido=informacion['apellido'], numeroDeDocumento=informacion['numeroDeDocumento'], vacunado=informacion['vacunado']) 

                  pasajero.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PasajeroFormulario() #Formulario vacio para construir el html
 
      return render(request, "AppTransporte/pasajeroFormulario.html", {"miFormulario":miFormulario})
  
def transporteFormulario(request):
        
      if request.method == 'POST':

            miFormulario = TransporteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  transporte = Transporte (tipo=informacion['tipo'], empresa=informacion['empresa'], capacidad=informacion['capacidad'], patente=informacion['patente']) 

                  transporte.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TransporteFormulario() #Formulario vacio para construir el html

      return render(request, "AppTransporte/transporteFormulario.html", {"miFormulario":miFormulario})
  
def terminalFormulario(request):
        
      if request.method == 'POST':

            miFormulario = TerminalFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  terminal = Terminal (nombre=informacion['nombre'], ubicacion=informacion['ubicacion']) 

                  terminal.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TerminalFormulario() #Formulario vacio para construir el html

      return render(request, "AppTransporte/terminalFormulario.html", {"miFormulario":miFormulario})  




# Create your views here.
def inicio(request):
    return render(request, "AppTransporte/inicio.html")
    
def pasajero(request):
    return render(request, "AppTransporte/pasajero.html")

def chofer(request):
    return render(request, "AppTransporte/chofer.html")

def transporte(request):
    return render(request, "AppTransporte/transporte.html")

def terminal(request):
    return render(request, "AppTransporte/terminal.html")

