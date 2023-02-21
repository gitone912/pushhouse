from random import randint
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.core.mail import send_mail

def auth_signin(request):
    template_name = 'authentication/layouts/aside/sign-in.html'

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "You Don't Have An Account, Please Sign Up")

    return render(request, template_name)


def auth_signup(request):
    if request.method != 'POST':
        return render(request, 'authentication/layouts/aside/sign-up.html')
    username = request.POST['username']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 != password2:
        messages.error(request, "Passwords do not match.")
        return redirect('/signup')

    user = User.objects.create_user(username=username, email=email, password=password1)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    login(request, user)
    return redirect('/')

def signout(request):
    logout(request)
    return redirect('signin')

def auth_reset_password(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # Generate OTP
            otp = randint(100000, 999999)
            # Send OTP to user's email
            send_mail(
                'Password Reset OTP',
                f'Your OTP for password reset is: {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            # Save OTP to the user's session
            request.session['reset_password_otp'] = otp
            request.session['reset_password_email'] = email
            return redirect('/reset-password-verify')
        else:
            messages.error(request, 'Email does not exist')
            return redirect('/reset-password')
    else:
        return render(request, 'authentication/layouts/aside/password-reset.html')


def auth_reset_password_verify(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method == 'POST':
        one = request.POST.get('1')
        two = request.POST.get('2')
        three = request.POST.get('3')
        four = request.POST.get('4')
        five = request.POST.get('5')
        six = request.POST.get('6')
        otp = one+two+three+four+five+six
        email = request.session.get('reset_password_email')
        session_otp = request.session.get('reset_password_otp')
      
        if str(otp) == str(session_otp):
            
            request.session['reset_password_email_verified'] = True
            return redirect('/new-password')
        else:
            messages.error(request, 'Invalid OTP')
            return redirect('/reset-password-verify/')
    else:
        return render(request, 'authentication/layouts/aside/two-steps.html')
    
def auth_new_password_view(request):
    if request.method == 'GET':
        return render(request, 'authentication/layouts/aside/new-password.html')
    elif request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        email = request.session.get('reset_password_email')
        user = User.objects.filter(email=email).first()
        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            # Delete reset password session variables
            del request.session['reset_password_email']
            del request.session['reset_password_otp']
            del request.session['reset_password_email_verified']
            return redirect('/signin')
        else:
            messages.error(request, 'Password does not match')
            return redirect('/new-password')



