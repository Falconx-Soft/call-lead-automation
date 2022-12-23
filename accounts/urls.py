from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
      path('', views.home, name="home"),
      path('login/', views.loginUser, name="login"),
      path('web-hook/', views.web_hook, name="web_hook"),
      path('change_password/', views.change_password, name="change_password"),
]



# http://localhost:8000/web-hook/?email=ibrahim.murad009@gmail.com&first_name=ibrahim&last_name=murad&phone_number=03344227779&total_debt_amount=50&zip_code=9999&state=Asia&age=25




 