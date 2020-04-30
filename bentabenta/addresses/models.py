from django.db import models

from billings.models import BillingProfile


ADDRESS_TYPE= (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
    )

# Create your models here.
class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.DO_NOTHING)
    address_type    = models.CharField(max_length=120, choices = ADDRESS_TYPE)
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120, null= True,blank=True)
    city            = models.CharField(max_length=120)
    country         = models.CharField(max_length=120)
    state           = models.CharField(max_length=120)
    postal_code     = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)