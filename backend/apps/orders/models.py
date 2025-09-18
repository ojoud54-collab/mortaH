from django.db import models
from django.conf import settings
class MerchantProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(blank=True)

class DriverProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    available_amount_daily = models.DecimalField(max_digits=12, decimal_places=0, default=0)

class Order(models.Model):
    STATUS_CHOICES = [('pending','pending'),('assigned','assigned'),('picked','picked'),('delivered','delivered'),('cancelled','cancelled')]
    merchant = models.ForeignKey(MerchantProfile, on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverProfile, on_delete=models.SET_NULL, null=True, blank=True)
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=50)
    invoice_number = models.CharField(max_length=100, blank=True, null=True)
    tracking_code = models.CharField(max_length=64, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)