from django.db import models


# Create your models here.

class Campaign(models.Model):
    tenantId = models.CharField(max_length=20, blank=False)
    buId = models.CharField(max_length=20)
    casaCampaignId = models.CharField(max_length=20, blank=False)


class Message(models.Model):
    content = models.CharField(max_length=2000, blank=False, default='')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)


class Customer(models.Model):
    tenantId = models.CharField(max_length=20, blank=False)
    buId = models.CharField(max_length=20)
    casaCustomerId = models.CharField(max_length=20, blank=False)


class CustomerMessage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete= models.CASCADE)