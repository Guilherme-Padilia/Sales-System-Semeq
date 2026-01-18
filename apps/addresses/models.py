from django.db import models

class Address(models.Model):
    id       = models.AutoField(primary_key=True)
    street   = models.CharField(max_length=100)
    city     = models.CharField(max_length=50)
    state    = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country  = models.CharField(max_length=50)
    number   = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'addresses'
