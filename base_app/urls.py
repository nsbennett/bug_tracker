from django.urls import path
from .views import submit_ticket, view_tickets, ticket_detailed_view

urlpatterns = [
    path('submit_ticket/', submit_ticket, name="ticket_page"),
    path('view_tickets/', view_tickets, name="user_tickets"),
    path('ticket_detail/<str:pk>', ticket_detailed_view, name="ticket_detail"),
]
