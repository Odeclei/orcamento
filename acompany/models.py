from django.db import models
from django.utils import timezone

# Create your models here.


class enterprise(models.Model):
    name = models.CharField(max_length=50)
    fantasyName = models.CharField(max_length=100, blank=True)
    cnpj = models.CharField(max_length=100, unique=True, blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
