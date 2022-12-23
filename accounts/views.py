from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Account
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

@login_required(login_url='login')
def home(request):

    if request.method == 'POST':
        form = CutomUserCreationForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    
    return render(request,'accounts/home.html')

@login_required(login_url='login')
def change_password(request):
    msg = ''
    if request.method == 'POST':
        print("**************")
        print(request.POST['new_password'])
        print(request.POST['confirm_password'])

        user = authenticate(request, email=request.user.email, password=request.POST['old_password']) # check password
        if user is not None:
            if len(request.POST['new_password']) >= 8 and request.POST['new_password'] == request.POST['confirm_password']:
                user.set_password(request.POST['new_password'])
                user.save()
                logout(request)
                return redirect('login')
            else:
                print("**************")
                msg = "New password mismatch"
        else:
            print("**************")
            msg = "Previous password is incorrect"
    context = {
        'msg': msg
    }
    return render(request,'accounts/change_password.html',context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    msg = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Account.objects.get(email=email)
            user = authenticate(request, email=email, password=password) # check password

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'Password is incorrect.'
        except:
            msg = 'User not recognized.'
    context = {
        'msg':msg,
        'title':'Login'
    }
    return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def web_hook(request):
    email               = request.GET['email']
    first_name          = request.GET['first_name']
    last_name           = request.GET['last_name']
    phone_number        = request.GET['phone_number']
    total_debt_amount   = request.GET['total_debt_amount']
    zip_code            = request.GET['zip_code']
    state               = request.GET['state']
    age                 = request.GET['age']

    password = Account.objects.make_random_password()

    userObj = Account.objects.create_user(email=email, password=password)
    userObj.save()

    userObj.first_name = first_name
    userObj.last_name = last_name
    userObj.phone_number = phone_number
    userObj.total_debt_amount = total_debt_amount
    userObj.zip_code = zip_code
    userObj.state = state
    userObj.age = age

    userObj.save()

    subject = 'Welcome'
    message = 'Link: http://'+request.META['HTTP_HOST']+'/\nEmail: '+email+'\nPassword: '+str(password)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

    
    return redirect('login')
    