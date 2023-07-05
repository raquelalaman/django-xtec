from django.db import models


class Customer(models.Model):
    customer_id = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=200)
    def __str__(self):
        return self.customer_name
    


class Account(models.Model):
    account_id = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    limit = models.IntegerField(default=0)

    def __str__(self):
        return self.description