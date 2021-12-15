from django import forms

    
class PasajeroFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    numeroDeDocumento = forms.IntegerField()
    vacunado = forms.BooleanField()

class ChoferFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    numeroDeDocumento = forms.IntegerField()
    numeroDeLicencia = forms.IntegerField()

class TransporteFormulario(forms.Form):
    tipo = forms.CharField() #Tipo: Aereo o terrestre
    empresa = forms.CharField() #Empresa a cargo
    capacidad = forms.IntegerField() #Capacidad del transporte
    patente = forms.IntegerField()

class TerminalFormulario(forms.Form):
    nombre = forms.CharField()
    ubicacion = forms.CharField()