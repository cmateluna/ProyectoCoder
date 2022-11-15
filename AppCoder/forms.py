from django import forms

class ProfesorFormulario(forms.Form):
    
    #Especificar los campos
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    # fecha_alta = forms.DateTimeField()
    
    
class EstudianteFormulario(forms.Form):
    
    nombre = forms.CharField(min_length=3,max_length=50)
    apellido = forms.CharField(min_length=3,max_length=50)
    email = forms.EmailField()
    