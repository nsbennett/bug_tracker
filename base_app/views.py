from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.urls import path, reverse
from .forms import TicketForm, CommentForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import CreateTicket, TicketComment
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
import slack_sdk as s
import environ
import requests
import json
from .pull_info import give_info

env = environ.Env()
environ.Env.read_env()


# Create your views here.

def post_notification_to_slack(message):
    webhook_url=env("SLACK_WEBHOOK")
    slack_data = {'text': message}

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

def view_home(request):
    """Renders homepage"""
    return render(request, 'home.html')

def loginPage(request):
    """Renders login page"""
    page = "login"

    if request.user.is_authenticated:
        return redirect("user_tickets")
    
    """Handles login"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_tickets')
        else:
            messages.error(request, "Username or password is incorrect.")

    return render(request, 'login_register.html')

"""Returns user to login page after logging out"""
def logoutPage(request):
    logout(request)
    messages.success(request, "User successfully logged out.")
    return redirect("login_page")

def registerUser(request):
    """Registers user"""
    page = "register"
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            group = Group.objects.get(name="user")
            user.username = user.username.lower()
            user.group = group
            user.save()

            messages.success(request, "User account created!")
            return redirect("login_page")
        
        else:
            messages.error(request, "An error has occurred during registration.")

    context = {"page": page,
               "form": form}
    return render(request, 'login_register.html', context)

"""All attempts at inappropriate login redirected to login page to avoid showing error messages"""
@login_required(login_url="login_page")
def submit_ticket(request):
    """Take user input from ticket submission and save to database"""
    ticket_form = TicketForm(request.POST)
    tech_info = give_info()
    context = {"ticket_form": ticket_form, "tech_info": tech_info,}
    if request.method == "POST":
        
        if ticket_form.is_valid():
            submission = ticket_form.save(commit=False)
            submission.ticket_author = request.user
            submission.save()
            new_ticket = CreateTicket.objects.first()
            messages.success(request, ("Done!"))
            for_slack = f"""
New ticket to review:
Time submitted: {new_ticket.timestamp}
Issue: {new_ticket.issue_category}

Subject: {new_ticket.message_subject}
Ticket: {new_ticket.message_body}
            """
            post_notification_to_slack(for_slack)
            return redirect('user_tickets')
        else:
            messages.error(request, "Error!")

    
    return render(request, "submit_ticket.html", context)

@login_required(login_url="login_page")
def view_tickets(request):
    """Show submitted tickets. This is the default place for users to reach after logging in.
    In absence of a user profile page, taking them directly to what they've done makes the most sense.
    """
    user = request.user
    
    if user.is_staff == True:
        tickets = CreateTicket.objects.all()

    else:
        tickets = CreateTicket.objects.filter(ticket_author=request.user.id)


    context = {
        "tickets": tickets,
    }
    return render(request, "view_tickets.html", context)


"""Redirect to login page to keep UX convenient"""
@login_required(login_url="login_page")
def ticket_detailed_view(request, pk):
    """View comments on ticket, reply to additional responses"""
    ticket = CreateTicket.objects.get(entry_id=pk)
    comments = TicketComment.objects.filter(ticket=pk)
    comment_form = CommentForm()
    ticket_form = TicketForm(instance=ticket)
    
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, instance=ticket)

        if ticket_form.is_valid():
            ticket_form.save()
            messages.success(request, ("Done!"))
            return redirect('ticket_detail', pk)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            obj = comment_form.save(commit=False)
            obj.ticket_id = pk
            obj.comment_author = request.user
            obj.save()
            post_notification_to_slack("Comment added to ticket.")
            messages.success(request, ("Done!"))
            return redirect('ticket_detail', pk)
            
        else:
            comment_form = CommentForm()

    context = {
        "ticket": ticket,
        "ticket_form": ticket_form,
        "comment_form": comment_form,
        "comments": comments,
    }

    return render(request, "view_single_ticket.html", context)


# Allows view of tickets in development account without requiring login
def view_development(request):
    """Provide a public-facing look at feature requests and completion status, no login required"""
    tickets = CreateTicket.objects.filter(ticket_author=9)

    context = {
        "tickets": tickets,
    }
    return render(request, "view_development.html", context)


# View specific development ticket
def view_dev_detail(request, pk):
    """Extension of view of development, but for specific features"""
    ticket = CreateTicket.objects.get(entry_id=pk)
    comments = TicketComment.objects.filter(ticket=pk)

    context = {
        "ticket": ticket,
        "comments": comments,
    }

    return render(request, "view_dev_details.html", context)


# Allows modification of user profile information
@login_required(login_url="login_page")
@transaction.atomic
def userProfile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect("user_profile")
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    
    
    context = {
        "user": request.user,
        "profile_form": profile_form,
    }
    return render(request, "profile_page.html", context)


# Creates the demo user login button on the home page
def oneClickDemoLogin(request):
    demo_user = env("DEMO_USER")
    demo_user_password = env("DEMO_USER_PASSWORD")
    thingie = User.objects.get(username=demo_user)
    # user = authenticate(request, username=demo_user, password=demo_user_password)
    login(request, thingie)
    tickets = CreateTicket.objects.filter(ticket_author=request.user.id)
    context = {
        "tickets": tickets,
    }
    return render(request, "view_tickets.html", context)