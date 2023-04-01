from django import forms
from django.forms import ModelForm
from .models import CreateTicket, TicketComment, Profile
from django.contrib.auth.forms import UserCreationForm
# from users.models import Profile

class TicketForm(ModelForm):
    class Meta:
        model = CreateTicket
        fields = ["ticket_status", "message_subject", "issue_category", "message_body"]


class CommentForm(ModelForm):

    class Meta:
        model = TicketComment
        fields = ["comment"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', "slack", "discord", "email")