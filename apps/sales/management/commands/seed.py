from django.core.management.base import BaseCommand

from ...models import Customer
from ....products.models import Product
from ....suppliers.models import Supplier

class Command(BaseCommand):
    def handle(self, *args, **options):
        supplier, _ = Supplier.objects.get_or_create(
            name='FORNECEDOR DE BEBIDAS',
            defaults={
                'email': 'guipadi28@gmail.com',
                'phone': '19992101463',
                'cnpj_cpf': '93427035000192', 
                'is_active': True
            }
        )
        
        secSupplier, _ = Supplier.objects.get_or_create(
            name='FORNECEDOR DE CARNE',
            defaults={
                'email': 'carnes@teste.com',
                'phone': '19999999999',
                'cnpj_cpf': '16227604000105', 
                'is_active': True
            }
        )

        Product.objects.get_or_create(
            name='COCA-COLA',
            defaults={
                'description': 'LATA 350ML',
                'price': 5.00,
                'supplier': supplier,
                'is_active': True
            }
        )
        
        Product.objects.get_or_create(
            name='PICANHA',
            defaults={
                'description': 'PICANHA 1KG',
                'price': 49.99,
                'supplier': secSupplier,
                'is_active': True
            }
        )

        Customer.objects.get_or_create(
            name='CLIENTE TESTE',
            defaults={
                'email': 'guipadi28@gmail.com',
                'phone': '19992101463',
                'is_active': True
            }
        )
        
        Customer.objects.get_or_create(
            name='CONSUMIDOR FINAL',
            defaults={
                'email': 'consumidor@teste.com',
                'phone': '19999999999',
                'is_active': True
            }
        )

