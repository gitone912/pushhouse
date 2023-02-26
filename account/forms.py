from django import forms
from .models import UserData
from django.forms import CheckboxInput, TextInput, widgets

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['full_name','company','contact_phone','company_site','country','communication','client_id','client_secret','token','structure','auth_code','allow_changes']
        widgets = {
                'full_name': TextInput(attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'enter full name',
                    'label': 'Full Name'
                }),
                'company': TextInput(attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'enter company',
                    'label': 'Company',
                }),
                'contact_phone': TextInput(attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'enter contact phone',
                    'label': 'Contact Phone',
                }),
                'company_site': TextInput(attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'enter company site',
                    'label': 'Company Site',
                }),
                'country': forms.Select(choices=UserData.COUNTRY_CHOICES, attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'select country',
                    'label': 'Country',
                }),
                'communication': forms.Select(choices=UserData.LANGUAGE_CHOICES, attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'select communication preference',
                    'label': 'Communication Preference',
                }),
                'client_id': TextInput(attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'enter client id',
                    'label': 'Client ID',
                }),
                'client_secret': TextInput(attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'enter client secret',
                    'label': 'Client Secret',
                }),
                'token': TextInput(attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'enter token',
                    'label': 'Token',
                }),
                'structure': TextInput(attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'enter structure',
                    'label': 'Structure',
                }),
                'auth_code': TextInput(attrs={
                    'class': "form-control form-control-lg form-control-solid",
                    'style': 'max-width: 300px;',
                    'placeholder': 'enter auth code',
                    'label': 'Auth Code',
                }),
                'allow_changes': CheckboxInput(attrs={
                    'class': "form-check-input w-45px h-30px",
                    'style': 'max-width: 300px;',
                    'placeholder': 'allow changes',
                    'label': 'Allow Changes',
                }),
            }
