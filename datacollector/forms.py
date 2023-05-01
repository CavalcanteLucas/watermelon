from .models import CustomerInfo
from django.forms import ModelForm
from django import forms


class CustomerStoreNameForm(forms.Form):
    class Meta:
        model = CustomerInfo
        fields = ['store_name']

TARGET_NETWORK_CHOICES = [
    ('polygon', 'Polygon'),
    ('etherium', 'Etherium'),
]
    

class CustomerTypeForm(forms.Form):
    customer_choices = forms.CharField(
        label="Customer Type", widget=forms.RadioSelect(choices=TARGET_NETWORK_CHOICES)
    )

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = "__all__"
