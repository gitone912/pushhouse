from django.urls import path
from . import views

urlpatterns = [
    path('billing/', views.billing_home, name='billing'),
    path('cancel-subscription/', views.cancel_subscription, name='cancel_subscription'),
    path('add-credit-card/', views.add_credit_card, name='add_credit_card'),
    path('billing/delete_card/<int:card_id>/', views.delete_credit_card, name='delete_credit_card'),
    path('billing/edit-card/<int:card_id>/', views.edit_credit_card, name='edit_credit_card'),
    path('billing/add-billing-address/', views.add_billing_address, name='add_billing_address'),
    path('billing/delete-billing-address/<int:address_id>/', views.delete_billing_address, name='delete_billing_address'),
    path('billing/edit-billing-address/<int:address_id>/', views.edit_billing_address, name='edit_billing_address'),


]