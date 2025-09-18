from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    role = models.CharField(max_length=20, choices=(('admin','admin'),('merchant','merchant'),('driver','driver'),('customer','customer')), default='customer')
    phone = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)