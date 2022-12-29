from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Account, Admin_Emails, User_offers
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from crm.models import *
from crm.api import *
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

    admin_email_list = []

    for user_obj in Admin_Emails.objects.all():
        admin_email_list.append(user_obj.email)

    domain = request.get_host()
    uid = urlsafe_base64_encode(force_bytes(userObj.pk))
    token = default_token_generator.make_token(userObj)

    subject = 'New user'
    message = "Link: "+ "http://"+domain+"/info/"+uid+"/"+token+"/"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = admin_email_list
    send_mail(subject, message, email_from, recipient_list)

    temp = requests.post('https://hook.us1.make.com/9emticn3exltfd6ws28mxrearlpn2r5p?formlink='+message+'&phone='+phone_number)
    print(temp.content,"<----------------------Web Hook Response")
    
    return redirect('login')
    
def info(request, uidb64, token):
    try:
        uid = int(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(id=uid)
    except:
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        if request.method == 'POST':
            form = CutomUserCreationForm(request.POST or None, instance=user)
            if form.is_valid():
                form.save()

                access_token_objs = access_token.objects.all()
                token_obj = access_token_objs[0]
                response = insert_records(token_obj.token, user, request.POST['xxTrustedFormCertUrl'])
                print(response)

                password = Account.objects.make_random_password()

                user.set_password(password)
                user.is_active = True
                user.save()

                subject = 'Welcome'
                message = 'Link: http://'+request.META['HTTP_HOST']+'/\nEmail: '+user.email+'\nPassword: '+str(password)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email,]
                send_mail(subject, message, email_from, recipient_list)

                return redirect('login')

            else:
                print(form.errors)
        context = {
            'user':user
        }
        return render(request,'accounts/confirm_info.html',context)
    else:
        return HttpResponse('There is a problem with the URL')

@login_required(login_url='login')
def offers(request):
    user_offers_obj = User_offers.objects.all()

    context = {
        'offers':user_offers_obj
    }

    return render(request, 'accounts/offers.html',context)
