from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.get_invoices),
    path('invoices/create/', views.create_invoice),
    path('invoices/update/<int:pk>/', views.update_invoice),
    path('invoices/delete/<int:pk>/', views.delete_invoice),
    path('invoice-details/', views.get_invoice_details),
    path('invoice-details/create/', views.create_invoice_detail),
    path('invoice-details/update/<int:pk>/', views.update_invoice_detail),
    path('invoice-details/delete/<int:pk>/', views.delete_invoice_detail),
]
