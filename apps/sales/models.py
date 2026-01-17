from django.db import models

class Sale(models.Model):
    id          = models.AutoField(primary_key=True)
    date        = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product_id  = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    address_id  = models.ForeignKey('addresses.Address', on_delete=models.CASCADE)
    quantity    = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status      = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'sales'

class Customer(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=100)
    email     = models.EmailField()
    phone     = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'customers'