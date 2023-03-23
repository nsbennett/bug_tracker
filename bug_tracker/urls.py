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
from base_app.views import view_home, view_development, view_dev_detail
# submit_comment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_home, name="home"),
    path('view_development', view_development, name="view_development"),
    path('view_development/<str:pk>', view_dev_detail, name="view_dev_detail"),
    path('', include('base_app.urls')),
    path('', include('users.urls')),
]
