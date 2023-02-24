from django.urls import path
from . import views

urlpatterns = [
    path('billing/', views.billing_home, name='billing'),
    path('cancel-subscription/', views.cancel_subscription, name='cancel_subscription'),
    path('add-credit-card/', views.add_credit_card, name='add_credit_card')

]