from django.test import TestCase
from decimal import Decimal

from apps.sales.models import Sale, SaleItem, SalePayment, Customer
from apps.addresses.models import Address
from apps.products.models import Product
from apps.suppliers.models import Supplier


class TestModels(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(
            name='Fornecedor Teste',
            email='supplier@test.com',
            phone='11999999999',
            is_active=True
        )

        self.product = Product.objects.create(
            name='Produto Teste',
            description='Descrição do produto',
            price=Decimal('10.00'),
            supplier=self.supplier,
            is_active=True
        )

        self.customer = Customer.objects.create(
            name='Cliente Teste',
            email='cliente@test.com',
            phone='11988888888',
            is_active=True
        )

        self.address = Address.objects.create(
            street='Rua Teste',
            city='São Paulo',
            state='SP',
            zip_code='01000-000',
            country='Brasil'
        )

    def test_create_sale(self):
        sale = Sale.objects.create(
            customer=self.customer,
            address=self.address,
            subtotal=Decimal('100.00'),
            total_sale=Decimal('100.00'),
            status='CONFIRMED'
        )

        self.assertIsNotNone(sale.id)
        self.assertEqual(sale.customer, self.customer)
        self.assertEqual(sale.total_sale, Decimal('100.00'))

    def test_create_sale_item(self):
        sale = Sale.objects.create(
            customer=self.customer,
            address=self.address,
            subtotal=Decimal('10.00'),
            total_sale=Decimal('10.00'),
            status='CONFIRMED'
        )

        item = SaleItem.objects.create(
            sale=sale,
            product=self.product,
            quantity=1,
            unit_price=Decimal('10.00'),
            total_price=Decimal('10.00')
        )

        self.assertIsNotNone(item.id)
        self.assertEqual(item.sale, sale)
        self.assertEqual(item.product, self.product)
        self.assertEqual(item.quantity, 1)

    def test_create_sale_payment(self):
        sale = Sale.objects.create(
            customer=self.customer,
            address=self.address,
            subtotal=Decimal('50.00'),
            total_sale=Decimal('50.00'),
            status='CONFIRMED'
        )

        payment = SalePayment.objects.create(
            sale=sale,
            payment_method='DIN',
            amount=Decimal('50.00')
        )

        self.assertIsNotNone(payment.id)
        self.assertEqual(payment.sale, sale)
        self.assertEqual(payment.amount, Decimal('50.00'))
