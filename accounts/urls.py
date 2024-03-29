from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
      path('', views.home, name="home"),
      path('info/<uidb64>/<token>/',views.info, name="info"),
      path('login/', views.loginUser, name="login"),
      path('web-hook/', views.web_hook, name="web_hook"),
      path('change_password/', views.change_password, name="change_password"),
      path('logout/', views.logoutUser, name="logout"),
      path('offers/', views.offers, name="offers"),
]



# http://localhost:8000/web-hook/?email=ibrahim.murad009@gmail.com&first_name=ibrahim&last_name=murad&phone_number=00000000&total_debt_amount=50&zip_code=9999&state=Asia&age=25

#https://koalafy.net/web-hook/?email=mikeydoo123@yahoo.com&first_name=Jill&last_name=Doe&phone_number=7324916475&total_debt_amount=17500&zip_code=&state=NJ&age=36




 