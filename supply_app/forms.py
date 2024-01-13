from django.forms import ModelForm
from django import forms
from .models import *


class InvoiceCreateForm(ModelForm):
    class Meta:

        model = Invoice
        fields = ['vendor', 'department', 'total', 'date']


class InvoiceFilterForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(
    ), required=False, label='Department', empty_label='Select Department')
    date_start = forms.DateField(required=False, label='Start date', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    date_end = forms.DateField(required=False, label='End date', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    vendor_name = forms.CharField(
        max_length=128, required=False, label='Vendor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['vendor_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['date_start'].widget.attrs.update(
            {'class': 'form-control selectpicker'})
        self.fields['date_end'].widget.attrs.update(
            {'class': 'form-control'})
