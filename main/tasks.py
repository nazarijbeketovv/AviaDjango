from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import Ticket


@shared_task
def send_ticket_email(ticket_id, user_email):
    # Здесь вы можете получить данные билета и сформировать содержимое письма
    ticket = Ticket.objects.get(id=ticket_id)
    subject = "Your E-Ticket"
    message = f"Thank you for your purchase. Your ticket details:\nFlight from {ticket.flight.origin} to {ticket.flight.destination}\nDeparture: {ticket.flight.departure}\nPrice: ${ticket.price}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
