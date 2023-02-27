from django.urls import path, include
from .models import Ticket
from django.contrib.auth.decorators import login_required
from .views import (
    HomeView,
    AddTicketView,
    TicketDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_ticket', AddTicketView.as_view(), name = 'add-ticket'),
    path('<int:pk>/detail', TicketDetailView.as_view(), name='ticket-detail'),
]
