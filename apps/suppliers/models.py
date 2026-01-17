from django.db import models

class Supplier(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=100)
    email     = models.EmailField()
    phone     = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'suppliers'