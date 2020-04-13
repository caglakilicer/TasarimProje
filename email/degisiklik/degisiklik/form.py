from django import forms
from .models import *
from django.contrib.auth.models import user

#değişiklik talep formu
class DegisiklikTalep(forms.Form):
    Gun = forms.CharField(required=True)
    Mevcut_Durum = forms.CharField(required=True)
    Talep = forms.CharField(required=True)
    Sebep = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
