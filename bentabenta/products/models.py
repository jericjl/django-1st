from django.db import models

# Create your models here.
class Products(models.Model):
    name        = models.CharField(max_length = 200)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2 ,max_digits=65)
    summary     = models.TextField(null=False)
    created_at  = models.DateTimeField(auto_now=True)