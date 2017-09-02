from django import forms
from .models import Word, Meaning

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('text',)
