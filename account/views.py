from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserDataForm
from .models import UserData
# Create your views here.

@login_required(login_url='/signin')
def user_data(request):
    try:
        user_data = request.user.userdata
    except UserData.DoesNotExist:
        user_data = None
    return render(request, 'account/overview.html', {'user_data': user_data})
@login_required(login_url='/signin')
def edit_user_data(request):
    try:
        user_data = request.user.userdata
    except UserData.DoesNotExist:
        user_data = UserData(user=request.user)
    form = UserDataForm(instance=user_data)
    if request.method == 'POST':
        form = UserDataForm(request.POST, instance=user_data)
        if form.is_valid():
            form.save()
            return redirect('/overview')
    return render(request, 'account/edit_profile.html', {'form': form})