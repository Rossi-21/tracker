from django.forms import ModelForm
from django import forms
from .models import *


class InvoiceCreateForm(ModelForm):
    class Meta:

        model = Invoice
        fields = ['vendor', 'department', 'total', 'date']
