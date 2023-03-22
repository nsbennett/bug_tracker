"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from base_app.forms import TicketForm
# from base_app.views import submit_ticket, view_tickets, ticket_detailed_view, loginPage, logoutPage, registerUser
# submit_comment

def ticket_page(request):
    return render(request, 'submit_ticket.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')),
    path('', include('users.urls')),
]
