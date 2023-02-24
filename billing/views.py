from django.shortcuts import redirect, render
from dashboard.models import Subscription
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CreditCard
from .forms import AddCreditCardForm
# Create your views here.
# def billing_home(request):
#     return render(request, "account/billing.html", {})

@login_required
def billing_home(request):
    user = request.user
    credit_cards = CreditCard.objects.filter(user=user)
    
    try:
        subscription = Subscription.objects.filter(user=user, end_date__gte=date.today()).order_by('end_date').first()
    except Subscription.DoesNotExist:
        subscription = None

    context = {
        'subscription': subscription,
        'credit_cards': credit_cards,
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
