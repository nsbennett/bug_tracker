import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CreateTicket(models.Model):
    """Create a ticket for support personnel to review"""
    # Need foreign key for user who posts it
    ticket_author = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    entry_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    timestamp = models.DateTimeField(default=timezone.now)
    message_subject = models.CharField(max_length=100)
    message_body = models.TextField()
    """Setting the values for dropdown select menu for what kind of issue user is facing"""
    CONNECTIVITY = "Connectivity"
    HARDWARE = "Hardware"
    SOFTWARE = "Software"
    THIRD_PARTY = "Bug in Third Party Integration"
    USER_ERROR = "User error"
    OTHER = "Other"
    ISSUE_CHOICES = [
        (CONNECTIVITY, "Connectivity"),
        (HARDWARE, "Hardware"),
        (SOFTWARE, "Software"),
        (THIRD_PARTY, "Third Party Integration"),
        (USER_ERROR, "User error"),
        (OTHER, "Other"),
    ]
    """The dropdown menu"""
    issue_category = models.CharField("Issue Category", max_length=100, blank=False, choices=ISSUE_CHOICES, default=OTHER)


    OPEN = "Open ticket"
    UNDER_REVIEW = "Under review"
    CLOSED = "Closed"

    ticket_status_choices = [
        (OPEN, "Open ticket"),
        (UNDER_REVIEW, "Under review"),
        (CLOSED, "Closed"),
    ]

    ticket_status = models.CharField("Ticket Status", max_length=100, blank=False, choices=ticket_status_choices, default=OPEN)

    class Meta:
        ordering = ("-timestamp",)

    def __str__(self):
        return self.message_subject
    
class TicketComment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ticket = models.ForeignKey(CreateTicket, on_delete=models.CASCADE, editable=False)
    comment_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    comment = models.TextField()

    class Meta:
        ordering = ('-timestamp',)
    # Add user ID of moderator, foreign key to user who posted ticket
    def __str__(self):
        if len(self.comment) > 50:
            return f"{str(self.comment)[:50]}..."
        else:
            return f"{str(self.comment)}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    slack = models.CharField(max_length=100, blank=True, null=True)
    discord = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()