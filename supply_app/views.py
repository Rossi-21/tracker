from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import *
from .forms import *


def home(request):
    # Get all invoices for the Database
    invoices = Invoice.objects.all()
    # Select form from forms.py for the view
    form = InvoiceFilterForm()
    # Sum Variable
    total_sum = 0

    if request.method == 'POST':
        # Grab the form for processing
        form = InvoiceFilterForm(request.POST)
        if form.is_valid():
            # Build the filter parameters based on form input
            filter_params = {}
            if form.cleaned_data['department']:
                filter_params['department__name__icontains'] = form.cleaned_data['department']
            if form.cleaned_data['date_start']:
                filter_params['date__gte'] = form.cleaned_data['date_start']
            if form.cleaned_data['date_end']:
                filter_params['date__lte'] = form.cleaned_data['date_end']
            if form.cleaned_data['vendor_name']:
                filter_params['vendor__name__icontains'] = form.cleaned_data['vendor_name']

            # Query the database with the filter parameters
            filtered_invoices = Invoice.objects.filter(**filter_params)

            if filtered_invoices:
                # Add the totals together to display the correct sum
                total_sum = round(filtered_invoices.aggregate(
                    Sum('total'))['total__sum'] or 0, 2)

            return render(request, 'index.html', {'invoices': filtered_invoices, 'form': form, 'total_sum': total_sum})

    context = {
        'invoices': invoices,
        'form': form,
        'total_sum': total_sum,
    }
    return render(request, 'index.html', context)


def createInvoice(request):
    # Select form from forms.py for the view
    form = InvoiceCreateForm()
    # Get the last three invoices form the database
    invoices = Invoice.objects.order_by('-id')[:3]

    if request.method == 'POST':
        # Grab the form for processing
        form = InvoiceCreateForm(request.POST)
        if form.is_valid():
            # If the form is valid save it to the database
            form.save()

            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'invoices': invoices
    }
    return render(request, 'createInvoice.html', context)


def invoiceTotalView(request):
    # Aggregate data by vendor and calculate the sum of invoice totals
    vendor_totals = Invoice.objects.values(
        'vendor__name').annotate(total_sum=Sum('total'))

    # Extract labels and data for Chart.js
    vendor_labels = [entry['vendor__name'] for entry in vendor_totals]
    total_sums = [entry['total_sum'] for entry in vendor_totals]

    context = {
        'vendor_labels': vendor_labels,
        'total_sums': total_sums,
    }
    return render(request, 'invoiceTotalView.html', context)


def invoiceDepartmentView(request):
    # Calulate total spend for each department
    department_totals = Invoice.objects.values(
        'department__name').annotate(total_spend=Sum('total'))
    # Remove departments with $0 spend
    department_totals = [
        entry for entry in department_totals if entry['total_spend'] > 0]
    # Extract data for Chart.js
    department_labels = [entry['department__name']
                         for entry in department_totals]
    total_spend = [entry['total_spend'] for entry in department_totals]

    context = {
        'department_labels': department_labels,
        'total_spend': total_spend
    }
    return render(request, 'invoiceDepartmentView.html', context)


def department_chart(request, department_name, template_name):
    # Get the Department
    department = Department.objects.get(name=department_name)
    # Retrieve invoices from the specified department
    invoices = Invoice.objects.filter(department=department).order_by('date')

    # Extract data for Chart.js
    dates = [invoice.date.strftime('%m-%d') for invoice in invoices]
    invoice_totals = [invoice.total for invoice in invoices]

    context = {
        'dates': dates,
        'invoice_totals': invoice_totals,
        'department_name': department.name
    }

    return render(request, template_name, context)


def storeSupplies(request):
    return department_chart(request, 'Store Supplies', 'storeSupplies.html')


def deli(request):
    return department_chart(request, 'Deli', 'deli.html')


def grocery(request):
    return department_chart(request, 'Grocery', 'grocery.html')


def meat(request):
    return department_chart(request, 'Meat', 'meat.html')
