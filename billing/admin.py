from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CreditCard

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'cardholder_name', 'card_type', 'card_number', 'expiration_date')
    list_filter = ('user',)
    search_fields = ('user__email', 'cardholder_name', 'card_type', 'card_number')

