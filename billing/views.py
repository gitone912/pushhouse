from django.shortcuts import redirect, render, get_object_or_404
from dashboard.models import Subscription
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CreditCard
from .forms import AddCreditCardForm,AddBillingAddressForm
from .models import BillingAddress
# Create your views here.
# def billing_home(request):
#     return render(request, "account/billing.html", {})

@login_required
def billing_home(request):
    user = request.user
    credit_cards = CreditCard.objects.filter(user=user)
    billing_addresses = BillingAddress.objects.filter(user=user)
    try:
        subscription = Subscription.objects.filter(user=user, end_date__gte=date.today()).order_by('end_date').first()
    except Subscription.DoesNotExist:
        subscription = None

    context = {
        'subscription': subscription,
        'credit_cards': credit_cards,
        'billing_addresses': billing_addresses,
    }
    return render(request, 'account/billing.html', context)

def cancel_subscription(request):
    if request.method == 'POST':
        subscription_id = request.POST.get('subscription_id')
        try:
            subscription = Subscription.objects.get(id=subscription_id, user=request.user)
            subscription.delete()
            messages.success(request, 'Subscription canceled successfully!')
        except Subscription.DoesNotExist:
            messages.error(request, 'Subscription not found.')
    return redirect('billing')




@login_required
def add_credit_card(request):
    if request.method == 'POST':
        form = AddCreditCardForm(request.POST)
        if form.is_valid():
            credit_card = form.save(commit=False)
            credit_card.user = request.user
            credit_card.last_4_digits = credit_card.card_number[-4:]
            credit_card.save()
            messages.success(request, 'Credit card added successfully.')
            return redirect('billing')
    else:
        form = AddCreditCardForm()

    context = {'form': form}
    return render(request, 'account/add_cc.html', context)

@login_required
def delete_credit_card(request, card_id):
    card = get_object_or_404(CreditCard, id=card_id)
    if card.user != request.user:
        messages.error(request, 'You do not have permission to delete this card.')
        return redirect('billing')
    card.delete()
    messages.success(request, 'Card deleted successfully.')
    return redirect('billing')

@login_required
def edit_credit_card(request, card_id):
    card = get_object_or_404(CreditCard, id=card_id)

    if request.method == 'POST':
        form = AddCreditCardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('billing')
    else:
        form = AddCreditCardForm(instance=card)

    context = {
        'form': form,
        'card_id': card_id,
    }

    return render(request, 'account/add_cc.html', context)

@login_required
def add_billing_address(request):
    form = AddBillingAddressForm(request.POST or None)
    if form.is_valid():
        billing_address = form.save(commit=False)
        billing_address.user = request.user
        billing_address.save()
        return redirect('billing')
    context = {
        'form': form
    }
    return render(request, 'account/add_address.html', context)

def delete_billing_address(request, address_id):
    address = get_object_or_404(BillingAddress, id=address_id, user=request.user)
    address.delete()
    return redirect('billing')

@login_required
def edit_billing_address(request, address_id):
    address = get_object_or_404(BillingAddress, id=address_id)

    if request.method == 'POST':
        form = AddBillingAddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('billing')
    else:
        form = AddBillingAddressForm(instance=address)

    context = {
        'form': form,
        'card_id': address_id,
    }

    return render(request, 'account/add_address.html', context)