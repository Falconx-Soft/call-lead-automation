from django.shortcuts import render
from .models import terms_and_condition, privacy_policy

# Create your views here.

def terms_and_conditions(request):

    terms_and_condition_obj = terms_and_condition.objects.all()

    context = {
        'terms_and_condition': terms_and_condition_obj[0]
    }

    return render(request,'terms_and_privacy/terms_and_conditions.html',context)

def privacy_and_policy(request):

    privacy_policy_obj = privacy_policy.objects.all()

    context = {
        'privacy_policy': privacy_policy_obj[0]
    }

    return render(request,'terms_and_privacy/privacy_policy.html',context)