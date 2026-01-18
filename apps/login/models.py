from django.db import models

class User(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=100)
    email     = models.EmailField(unique=True)
    password  = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'
