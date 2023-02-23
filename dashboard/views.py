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
    if request.method == 'POST':
        selected_plan = request.POST.get('plan')
        if selected_plan:
            plan = Plan.objects.get(pk=selected_plan)
            start_date = date.today()
            end_date = start_date + timedelta(days=30) # 30-day subscription
            subscription = Subscription.objects.create(user=request.user, plan=plan, start_date=start_date, end_date=end_date)
            return redirect('/project_dashboard', subscription_id=subscription.id)
    return render(request, 'monthly_plan.html', {'plans': plans})

def select_yearly_plan(request):
    plans = Plan.objects.all()
    if request.method == 'POST':
        selected_plan = request.POST.get('plan')
        if selected_plan:
            plan = Plan.objects.get(pk=selected_plan)
            start_date = date.today()
            end_date = start_date + timedelta(days=30) # 30-day subscription
            subscription = Subscription.objects.create(user=request.user, plan=plan, start_date=start_date, end_date=end_date)
            return redirect('/project_dashboard', subscription_id=subscription.id)
    return render(request, 'yearly_plan.html', {'plans': plans})