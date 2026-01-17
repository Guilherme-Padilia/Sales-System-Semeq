from django.db import models

class Sale(models.Model):
    id         = models.AutoField(primary_key=True)
    date       = models.DateTimeField(auto_now_add=True)
    customer   = models.ForeignKey('Customer', on_delete=models.CASCADE)
    address    = models.ForeignKey('addresses.Address', on_delete=models.CASCADE)
    subtotal   = models.DecimalField(max_digits=10, decimal_places=2)
    total_sale = models.DecimalField(max_digits=10, decimal_places=2)
    status     = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'sales'
        
class SaleItem(models.Model):
    id          = models.AutoField(primary_key=True)
    sale        = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product     = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity    = models.IntegerField()
    unit_price  = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status      = models.CharField(max_length=20)
    
    class Meta:        
        db_table = 'sale_items'
        
class SalePayment(models.Model):
    id             = models.AutoField(primary_key=True)
    sale           = models.ForeignKey(Sale, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)
    amount         = models.DecimalField(max_digits=10, decimal_places=2)
    is_active      = models.CharField(max_length=20)

class Customer(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=100)
    email     = models.EmailField()
    phone     = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'customers'