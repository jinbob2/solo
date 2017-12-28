from django import forms

# from .models import Board
from .models import Bord

class BordForm(forms.ModelForm):
    class Meta:
        model = Bord
        fields = ['title', 'image', 'embed_code', 'description', 'check']


