from datetime import date
from django import forms
from django.core.validators import RegexValidator
from .models import CreditCard
from django.forms import widgets

class AddCreditCardForm(forms.ModelForm):
    card_number = forms.CharField(
        max_length=16,
        validators=[
            RegexValidator(r'^\d{16}$', 'Card number must be 16 digits')
        ]
    )
    cardholder_name = forms.CharField(max_length=255)
    cvv = forms.CharField(max_length=3)
    expiration_date = forms.DateField(initial=date.today)
    card_type = forms.ChoiceField(choices=CreditCard.CARD_TYPES)
    class Meta:
        model = CreditCard
        fields = ('cardholder_name', 'card_number', 'card_type', 'expiration_date')
        widgets = {
            'cardholder_name': forms.TextInput(attrs={
                'class': "form-control form-control-lg form-control-solid",
                'style': 'max-width: 300px;',
                'placeholder': 'enter Cardholder name',
                'label': 'Cardholder Name'
            }),
            'card_number': forms.TextInput(attrs={
                'class': "form-control form-control-lg form-control-solid",
                'style': 'max-width: 300px;',
                'placeholder': 'enter Card Number',
                'label': 'Card Number'
            }),
            'card_type': forms.Select(attrs={
                'class': "form-control form-control-lg form-control-solid",
                'style': 'max-width: 300px;',
                'label': 'Card Type'
            }),
            'expiration_date': forms.DateInput(attrs={
                'class': "form-control form-control-lg form-control-solid",
                'style': 'max-width: 300px;',
                'label': 'Expiration Date',
                'type': 'date'
            }),
        }
