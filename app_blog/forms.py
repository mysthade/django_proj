# В forms.py

from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = '__all__'
    
    image = forms.FileField()
