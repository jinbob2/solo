from django import forms

from .models import Bord

class BordForm(forms.ModelForm):
    class Meta:
        model = Bord
        fields = [ 'check','title','image','description','embed_code']