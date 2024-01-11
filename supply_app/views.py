from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    invoices = Invoice.objects.all()

    context = {
        'invoices': invoices
    }
    return render(request, 'index.html', context)
