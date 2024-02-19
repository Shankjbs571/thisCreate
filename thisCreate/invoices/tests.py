from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class InvoiceTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        response = self.client.post('/api/invoices/create/', {
            "date": "2022-03-01",
            "customer_name": "John Doe test case 2"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoices(self):
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_invoice(self):
    #     response = self.client.put('/api/invoices/update/2/', {
    #         "date": "2022-03-02",
    #         "customer_name": "Jane Doefrom test original 2 now updated"
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_delete_invoice(self):
    #     response = self.client.delete('/api/invoices/delete/1/')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class InvoiceDetailTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    # def test_create_invoice_detail(self):
    #     response = self.client.post('/api/invoice-details/create/', {
    #         "invoice": 2,
    #         "description": "inv detail reference form test creation",
    #         "quantity": 1,
    #         "unit_price": 100,
    #         "price": 100
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice_details(self):
        response = self.client.get('/api/invoice-details/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_invoice_detail(self):
    #     response = self.client.put('/api/invoice-details/update/2/', {
    #         "description": "inv detail reference update after 1",
    #         "quantity": 2,
    #         "unit_price": 150,
    #         "price": 300
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_delete_invoice_detail(self):
    #     response = self.client.delete('/api/invoice-details/delete/1/')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
