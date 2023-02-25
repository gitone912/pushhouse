from datetime import date
from django import forms
from django.core.validators import RegexValidator
from .models import CreditCard, BillingAddress
from django.forms import widgets


class AddCreditCardForm(forms.ModelForm):
    card_number = forms.CharField(
        max_length=16,
        validators=[
            RegexValidator(r'^\d{16}$', 'Card number must be 16 digits')
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'enter Card Number',
            'label': 'Card Number'
        })
    )
    cardholder_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'enter Cardholder name',
            'label': 'Cardholder Name'
        })
    )
    cvv = forms.CharField(
        max_length=3,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 100px;',
            'placeholder': 'CVV',
            'label': 'CVV'
        })
    )
    expiration_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'type': 'date'
        }),
        required=True
    )
    card_type = forms.ChoiceField(choices=CreditCard.CARD_TYPES, widget=forms.Select(attrs={
        'class': 'form-control form-control-lg form-control-solid',
        'style': 'max-width: 200px;',
        'label': 'Card Type'
    }))
    
    class Meta:
        model = CreditCard
        fields = ('cardholder_name', 'card_number', 'card_type', 'expiration_date')

class AddBillingAddressForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'Full Name',
            'label': 'Full Name'
        })
    )
    company_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'Company Name',
            'label': 'Company Name'
        })
    )
    address_line_1 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'Address Line 1',
            'label': 'Address Line 1'
        })
    )
    address_line_2 = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'Address Line 2',
            'label': 'Address Line 2'
        })
    )
    city = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'City',
            'label': 'City'
        })
    )
    state = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'State',
            'label': 'State'
        })
    )
    postal_code = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'Postal Code',
            'label': 'Postal Code'
        })
    )
    country = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'Country',
            'label': 'Country'
        })
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'style': 'max-width: 300px;',
            'placeholder': 'Phone Number',
            'label': 'Phone Number'
        })
    )
    is_default = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    class Meta:
        model = BillingAddress
        fields = ('full_name', 'company_name', 'address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', 'phone_number', 'is_default')

