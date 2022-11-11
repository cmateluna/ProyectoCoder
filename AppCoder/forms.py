from django import forms

class ProfesorFormulario(forms.Form):
    
    #Especificar los campos
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    fecha_alta = forms.DateTimeField()