from django.contrib import admin
from .models import terms_and_condition, privacy_policy
# Register your models here.

admin.site.register(terms_and_condition)
admin.site.register(privacy_policy)