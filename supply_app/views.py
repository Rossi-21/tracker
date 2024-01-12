from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    invoices = Invoice.objects.all()
    form = InvoiceFilterForm()
    if request.method == 'POST':
        form = InvoiceFilterForm(request.POST)
        if form.is_valid():
            # Build the filter parameters based on form input
            filter_params = {}
            if form.cleaned_data['total_gt']:
                filter_params['total__gt'] = form.cleaned_data['total_gt']
            if form.cleaned_data['date_start']:
                filter_params['date__gte'] = form.cleaned_data['date_start']
            if form.cleaned_data['date_end']:
                filter_params['date__lte'] = form.cleaned_data['date_end']
            if form.cleaned_data['vendor_name']:
                filter_params['vendor__name__icontains'] = form.cleaned_data['vendor_name']

            # Query the database with the filter parameters
            filtered_invoices = Invoice.objects.filter(**filter_params)

            return render(request, 'index.html', {'invoices': filtered_invoices, 'form': form})

    context = {
        'invoices': invoices,
        'form': form,
    }
    return render(request, 'index.html', context)
