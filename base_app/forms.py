from django import forms
from django.forms import ModelForm
from .models import CreateTicket, TicketComment
from django.contrib.auth.forms import UserCreationForm
# from users.models import Profile

class TicketForm(ModelForm):
    class Meta:
        model = CreateTicket
        fields = ["message_subject", "issue_category", "message_body"]


class CommentForm(ModelForm):

    class Meta:
        model = TicketComment
        fields = ["comment"]


# class TicketClosingForm(ModelForm):

#     class Meta:
#         model = TicketClosed
#         fields = ["ticket_status"]

# class ProfileCreationForm(UserCreationForm):

#     class Meta:
#         model = Profile
#         fields = ["name", "user", "email", "password1", "password2"]