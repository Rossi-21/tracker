from django.forms import ModelForm
from django import forms
from .models import *


class InvoiceCreateForm(ModelForm):
    class Meta:

        model = Invoice
        fields = ['vendor', 'department', 'total', 'date']


class InvoiceFilterForm(forms.Form):
    total_gt = forms.FloatField(required=False, label='Total greater than')
    date_start = forms.DateField(required=False, label='Start date')
    date_end = forms.DateField(required=False, label='End date')
    vendor_name = forms.CharField(
        max_length=128, required=False, label='Vendor name')
