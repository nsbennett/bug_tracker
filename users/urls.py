from django.urls import path
from django.shortcuts import render
from base_app.views import loginPage, logoutPage, registerUser, userProfile, oneClickDemoLogin


def ticket_page(request):
    return render(request, 'submit_ticket.html')

urlpatterns = [
    path('login/', loginPage, name="login_page"),
    path('logout/', logoutPage, name="logout"),
    path('register/', registerUser, name="register"),
    path('user_profile/', userProfile, name="user_profile"),
    path('demo_login/', oneClickDemoLogin, name="one_click_demo_login"),
]