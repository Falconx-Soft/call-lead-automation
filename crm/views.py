from django.shortcuts import render, redirect

from .api import insert_records
from .models import access_token


# Create your views here.

def add_to_crm(request):
    if request.method == 'POST':
        # print(request.POST['xxTrustedFormCertUrl'])
        # print(request.POST['xxTrustedFormPingUrl'])
        access_token_objs = access_token.objects.all()
        token_obj = access_token_objs[0]
        response = insert_records(token_obj.token, request.user, request.POST['xxTrustedFormCertUrl'])
        print(response)
    return redirect('home')
