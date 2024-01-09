from django import forms
from .models import TokenPurchase


class TokenPurchaseForm(forms.ModelForm):
    class Meta:
        model = TokenPurchase
        fields = ['quantity']
