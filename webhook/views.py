from django.shortcuts import render
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import webhook_data
# Create your views here.

@csrf_exempt
def data(request):
    json_data = json.loads(request.body)
    webhook_data_obj = webhook_data.objects.create(data=json_data)
    webhook_data_obj.save()
    return JsonResponse({'status':200})