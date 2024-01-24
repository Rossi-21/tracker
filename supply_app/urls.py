from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.createInvoice, name="create-invoice"),
    path('data/', views.viewData, name="view-data")
]
