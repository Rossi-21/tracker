from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.createInvoice, name="create-invoice"),
    path('data/total', views.invoiceTotalView, name="invoice-total-view"),
    path('data/department', views.invoiceDepartmentView,
         name="invoice-department-view"),

]
