from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    phone = models.CharField("Phone", max_length=32, blank=True)

    date_of_birth = models.DateField("Date of birth", null=True, blank=True)

    address_line1 = models.CharField("Address line 1", max_length=255, blank=True)
    address_line2 = models.CharField("Address line 2", max_length=255, blank=True)
    city = models.CharField("City", max_length=120, blank=True)
    postcode = models.CharField("Postcode", max_length=20, blank=True)
    country = models.CharField("Country", max_length=2, blank=True)

    def __str__(self) -> str:
        return self.username or self.email