from django import forms
from main.models import Contact

class Contactform(forms.ModelForm):
    class Meta:
        model= Contact
        fields=['name','email','message']