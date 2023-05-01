import enum
from django.db import models

class CustomerInfo(models.Model):

    store_name = models.CharField(max_length=200)
    balance_left = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    # target_network = models.RadioButtonField(choices=TARGET_NETWORK_CHOICES)
    target_address = models.CharField(max_length=200)
    client_address = models.CharField(max_length=200)
