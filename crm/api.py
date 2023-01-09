import requests
import json

from .keys import client_id, client_secret_id, refresh_token
from .models import access_token

def get_refresh_token():
    url = 'https://accounts.zoho.com/oauth/v2/token?refresh_token='+refresh_token+'&client_id='+client_id+'&client_secret='+client_secret_id+'&grant_type=refresh_token'

    response = requests.post(url=url)
    refres_response = response.json()
    return refres_response['access_token']


def insert_records(token,user,trusted_form_url):
    url = 'https://www.zohoapis.com/crm/v2/Leads'

    headers = {
        'Authorization': 'Zoho-oauthtoken '+token,
    }

    request_body = dict()
    record_list = list()

    record_object_1 = {
        'Email': user.email,
        'Last_Name': user.last_name,
        'First_Name': user.first_name,
        'Debt_Amount': str(user.total_debt_amount),
        "Phone": user.phone_number,
        "State": user.state,
        "xxTrustedFormCerUrl": trusted_form_url,
        "Age": str(user.age),
        "Lead_Source": "https://koalafy.net/",
    }

    record_list.append(record_object_1)

    request_body['data'] = record_list

    trigger = [
        'approval',
        'workflow',
        'blueprint'
    ]

    request_body['trigger'] = trigger

    response = requests.post(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        print(response.json())
        temp = response.json()
        try:
            if temp['data'][0]['code'] == 'SUCCESS':
                return 'SUCCESS'
            else:
                return 'Error'
        except Exception as e:
            print("----->",e)
            refresh_token =  get_refresh_token()
            access_token_objs = access_token.objects.all()
            token_obj = access_token_objs[0]
            token_obj.token = refresh_token
            token_obj.save()
            insert_records(token_obj.token,user,trusted_form_url)
    else:
        return "Error"