from django import forms
from blog.models import crudst, crudst1

class stform(forms.ModelForm):
    class Meta:
        model=crudst
        fields="__all__"

class stform1(forms.ModelForm):
    class Meta:
        model=crudst1
        fields="__all__"
        