from datetime import datetime, timedelta
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .models import Plan, Subscription

# Create your views here.
@login_required(login_url='/signin')
def dashboard(request):
    return render(request, 'index.html')

def project_dashboard(request):
    return render(request, 'dashboards/projects.html')


@login_required
def select_monthly_plan(request):
    plans = Plan.objects.all()
    subscription = Subscription.objects.filter(user=request.user).first()
    if request.method == 'POST':
        selected_plan_id = request.POST.get('plan')
        if selected_plan_id:
            selected_plan = Plan.objects.get(pk=selected_plan_id)
            start_date = date.today()
            end_date = start_date + timedelta(days=selected_plan.duration)
            if subscription:
                subscription.plan = selected_plan
                subscription.start_date = start_date
                subscription.end_date = end_date
                subscription.save()
            else:
                subscription = Subscription.objects.create(user=request.user, plan=selected_plan, start_date=start_date, end_date=end_date)
            return redirect('/project_dashboard', subscription_id=subscription.id)
    return render(request, 'monthly_plan.html', {'plans': plans})


@login_required
def select_yearly_plan(request):
    plans = Plan.objects.all()
    subscription = Subscription.objects.filter(user=request.user).first()
    if request.method == 'POST':
        selected_plan_id = request.POST.get('plan')
        if selected_plan_id:
            selected_plan = Plan.objects.get(pk=selected_plan_id)
            start_date = date.today()
            end_date = start_date + timedelta(days=selected_plan.duration)
            if subscription:
                subscription.plan = selected_plan
                subscription.start_date = start_date
                subscription.end_date = end_date
                subscription.save()
            else:
                subscription = Subscription.objects.create(user=request.user, plan=selected_plan, start_date=start_date, end_date=end_date)
            return redirect('/project_dashboard', subscription_id=subscription.id)
    return render(request, 'yearly_plan.html', {'plans': plans})