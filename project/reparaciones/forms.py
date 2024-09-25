from django import forms
from .models import Reparacion

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = ['descripcion', 'costo', 'fecha_reparacion', 'imagen']
