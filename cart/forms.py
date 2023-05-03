from django import forms
from .models import ShippingAdress

class ShippingAdressForm(forms.ModelForm):
    class Meta:
        model = ShippingAdress
        fields = ['address', 'city', 'state', 'state', 'zip_code']