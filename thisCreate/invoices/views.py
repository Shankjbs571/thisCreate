from django.shortcuts import render

# Create your views here.
# from rest_framework import viewsets
# from .models import Invoice, InvoiceDetail
# from .serializers import InvoiceSerializer, InvoiceDetailSerializer

# class InvoiceViewSet(viewsets.ModelViewSet):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer

# class InvoiceDetailViewSet(viewsets.ModelViewSet):
#     queryset = InvoiceDetail.objects.all()
#     serializer_class = InvoiceDetailSerializer

# invoices/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

# Views for Invoice
@api_view(['GET'])
def get_invoices(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_invoice(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_invoice(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
        print("try done")
    except Invoice.DoesNotExist:
        print("inside 404 except")
        return Response(status=404)
    
    serializer = InvoiceSerializer(invoice, data=request.data)
    print("serializer: ",serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_invoice(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=404)
    
    invoice.delete()
    return Response(status=204)

# Views for InvoiceDetail
@api_view(['GET'])
def get_invoice_details(request):
    invoice_details = InvoiceDetail.objects.all()
    serializer = InvoiceDetailSerializer(invoice_details, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_invoice_detail(request):
    serializer = InvoiceDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_invoice_detail(request, pk):
    try:
        invoice_detail = InvoiceDetail.objects.get(pk=pk)
    except InvoiceDetail.DoesNotExist:
        return Response(status=404)
    
    serializer = InvoiceDetailSerializer(invoice_detail, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_invoice_detail(request, pk):
    try:
        invoice_detail = InvoiceDetail.objects.get(pk=pk)
    except InvoiceDetail.DoesNotExist:
        return Response(status=404)
    
    invoice_detail.delete()
    return Response(status=204)

