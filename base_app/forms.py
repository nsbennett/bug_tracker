from django import forms
from django.forms import ModelForm
from .models import CreateTicket, TicketComment, Profile
from django.contrib.auth.forms import UserCreationForm

# Creates the form for "submit new ticket"
class TicketForm(ModelForm):
    class Meta:
        model = CreateTicket
        fields = ["ticket_status", "message_subject", "issue_category", "message_body"]


# Creates comment field for tickets
class CommentForm(ModelForm):

    class Meta:
        model = TicketComment
        fields = ["comment"]


# Gives user ability to add other intformation, so far unused
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', "slack", "discord", "email")