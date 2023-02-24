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
