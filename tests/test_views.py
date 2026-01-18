from django.test import TestCase, Client

class TestViews(TestCase):
    def test_search_customers(self):
        self.client = Client()
        response = self.client.get('/sales/search-customers/') 
        
        self.assertEqual(response.status_code, 200)
        
    def test_search_products(self):
        self.client = Client()
        response = self.client.get('/products/search/') 
        
        self.assertEqual(response.status_code, 200)
        