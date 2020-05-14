from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError
from django.template.defaulttags import comment

from models import Destino


class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ['nombre', 'compania', 'tipo', 'afluencia',
                  'precio', 'tipoTurismo', 'descripcion', 'coordenadas', 'description', 'link']
