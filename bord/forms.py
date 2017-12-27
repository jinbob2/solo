from django import forms

from .models import Bord

class BordForm(forms.ModelForm):
    class meta:
        model = Bord
        fields = ['title','image','embed_code','description','check']

