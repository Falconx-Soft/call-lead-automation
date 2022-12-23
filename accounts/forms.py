from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.forms import ModelForm

class CutomUserCreationForm(ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name','phone_number', 'total_debt_amount', 'zip_code', 'state', 'age']

        def __init__(self, *args, **kwargs):
            super(CutomUserCreationForm, self).__init__(*args, **kwargs)