from django import forms
from .models import Avenger

class HerosForm(forms.ModelForm):
    class Meta:

        model = Avenger
        fields = ['decs', 'img']
