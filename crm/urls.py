from django.urls import path
from . import views

urlpatterns = [
      path('add-to-crm', views.add_to_crm, name="add_to_crm"),
]