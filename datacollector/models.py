from django.db import models


class CustomerInfo(models.Model):
    store_name = models.CharField(max_length=200, null=True)
    balance_left = models.IntegerField(default=0, null=True)
    selling_price = models.IntegerField(default=0, null=True)
    target_network = models.CharField(max_length=200, null=True)
    target_address = models.CharField(max_length=200, null=True)
    client_email = models.EmailField(max_length=200, null=True)
