from django.forms import ModelForm
from django import forms
from .models import *


class InvoiceCreateForm(ModelForm):
    class Meta:
        # Select your model
        model = Invoice
        # Choose the fields you want to show
        fields = ['vendor', 'department', 'total', 'date']

        # Apply Bootstrap CSS
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['department'].widget.attrs.update(
                {'class': 'form-control'})
            self.fields['vendor'].widget.attrs.update(
                {'class': 'form-control'})
            self.fields['total'].widget.attrs.update(
                {'class': 'form-control'})
            self.fields['date'].widget.attrs.update(
                {'class': 'form-control'})


class InvoiceFilterForm(forms.Form):
    # Set the form fields
    department = forms.ModelChoiceField(queryset=Department.objects.all(
    ), required=False, label='Department', empty_label='Select Department')
    date_start = forms.DateField(required=False, label='Start date', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    date_end = forms.DateField(required=False, label='End date', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    vendor_name = forms.ModelChoiceField(queryset=Vendor.objects.all(
    ), required=False, label='Vendor', empty_label="Select Vendor")

    # Apply Bootstrap CSS
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['vendor_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['date_start'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['date_end'].widget.attrs.update(
            {'class': 'form-control'})
