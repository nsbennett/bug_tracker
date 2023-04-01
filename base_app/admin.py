from django.contrib import admin
from .models import CreateTicket, TicketComment, Profile

# Register your models here.
admin.site.register(CreateTicket)
admin.site.register(TicketComment)
admin.site.register(Profile)
