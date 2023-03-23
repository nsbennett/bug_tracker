from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.urls import path, reverse
from .forms import TicketForm, CommentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import CreateTicket, TicketComment
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required

# from users.models import Profile

# Create your views here.

def loginPage(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("user_tickets")
    
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

def logoutPage(request):
    logout(request)
    messages.success(request, "User successfully logged out.")
    return redirect("login_page")

def registerUser(request):
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

@login_required(login_url="login_page")
# @permission_required("base_app.add_create_ticket", login_url="login_page")
def submit_ticket(request):
    """Take user input from ticket submission and save to database"""
    ticket_form = TicketForm(request.POST)
    context = {"ticket_form": ticket_form}
    if request.method == "POST":
        
        if ticket_form.is_valid():
            submission = ticket_form.save(commit=False)
            submission.ticket_author = request.user
            # ticket_form = TicketForm()
            submission.save()
            # ticket_status = TicketClosed(ticket_reference=submission, ticket_status="OPEN")
            # ticket_status.save()
            messages.success(request, ("Done!"))
            return redirect('user_tickets')
        else:
            messages.error(request, "Error!")

    
    return render(request, "submit_ticket.html", context)

@login_required(login_url="login_page")
# @permission_required("base_app.view_view_tickets", login_url="login_page")
def view_tickets(request):
    """Show submitted tickets"""
    user = request.user
    
    if user.is_staff == True:
        tickets = CreateTicket.objects.all()
    #     for ticket in tickets:
    #         ticket_status = TicketClosed.objects.filter(ticket.entry_id)

    else:
        tickets = CreateTicket.objects.filter(ticket_author=request.user.id)
    #     for ticket in tickets:
    #         ticket_status = TicketClosed.objects.filter(ticket.entry_id)


    # ticket_status = TicketClosed.objects.all().values()

    context = {
        "tickets": tickets,
        # "ticket_status": ticket_status,
    }
    return render(request, "view_tickets.html", context)



@login_required(login_url="login_page")
# @permission_required("base_app.view_ticket_comment", login_url="login_page")
def ticket_detailed_view(request, pk):
    ticket = CreateTicket.objects.get(entry_id=pk)
    comments = TicketComment.objects.filter(ticket=pk)
    comment_form = CommentForm()
    # ticket_status = TicketClosed.objects.get(ticket_reference=pk)
    # ticket_status_form = TicketClosingForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            obj = comment_form.save(commit=False)
            obj.ticket_id = pk
            obj.comment_author = request.user
            obj.save()
            messages.success(request, ("Done!"))
            return redirect('ticket_detail', pk)
            
        else:
            comment_form = CommentForm()

    # if request.method == "POST":
    #     ticket_status_form = TicketClosingForm(request.POST)

    #     if ticket_status_form.is_valid():
    #         obj = ticket_status_form.save(commit=False)
            # ticket_status = obj
            # obj.ticket_reference = ticket
            # ticket_status.save()
        #     ticket_status.ticket_status = obj.ticket_status
        #     ticket_status.save()
        #     messages.success(request, ("Done!"))
        #     return redirect('ticket_detail', pk)
            
        # else:
        #     ticket_status_form = TicketClosingForm()

    context = {
        "ticket": ticket,
        "comment_form": comment_form,
        "comments": comments,
        # "ticket_status": ticket_status,
        # "ticket_status_form": ticket_status_form,
    }

    return render(request, "view_single_ticket.html", context)

