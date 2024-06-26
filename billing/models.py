from django.db import models
from django.conf import settings


class CreditCard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    last_4_digits = models.CharField(max_length=4,null=True, blank=True)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)
    CARD_TYPES = [
        ('visa', 'visa'),
        ('mastercard', 'mastercard'),
        ('discover', 'discover'),
        ('american-express', 'american-express'),
        ('Other', 'Other'),
    ]
    card_type = models.CharField(max_length=20, choices=CARD_TYPES)

    def __str__(self):
        return f"{self.card_type} ending in {self.card_number[-4:]}"

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Billing addresses"

    def __str__(self):
        return f"{self.user.username}'s billing address: {self.full_name}, {self.city}, {self.country}"
