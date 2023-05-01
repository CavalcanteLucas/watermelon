from django.db import models


class CustomerInfo(models.Model):
    store_name = models.CharField(max_length=200, null=True)
    balance_left = models.IntegerField(default=0, null=True)
    selling_price = models.IntegerField(default=0, null=True)
    target_network = models.CharField(max_length=200, null=True)
    target_address = models.CharField(max_length=200, null=True)
    client_email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return (
            f"{self.store_name},"
            f"{self.balance_left},"
            f"{self.selling_price},"
            f"{self.target_network},"
            f"{self.target_address},"
            f"{self.client_email}"
        )
