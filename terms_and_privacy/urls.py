from django.urls import path

from . import views

urlpatterns = [
      path('terms_and_conditions/', views.terms_and_conditions, name="terms_and_conditions"),
      path('privacy_policy/', views.privacy_and_policy, name="privacy_policy"),
]
