from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .tasks import send_ticket_email
from .forms import FlightSearchForm, PassengerForm, PaymentForm
from .models import Flight, Passenger, Ticket
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings


def index(request):
    return render(request, "main/index.html")


def search_flights(request):
    form = FlightSearchForm(request.GET or None)
    tickets = []

    if form.is_valid():
        origin = form.cleaned_data["origin"]
        destination = form.cleaned_data["destination"]
        departure = form.cleaned_data["departure"]

        flights = Flight.objects.filter(
            origin=origin, destination=destination, departure__date=departure
        )
        tickets = Ticket.objects.filter(flight__in=flights)

    paginator = Paginator(tickets, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "main/results.html",
        {
            "form": form,
            "tickets": tickets,
            "page_obj": page_obj,
            "origin": request.GET.get("origin", ""),
            "destination": request.GET.get("destination", ""),
            "departure": request.GET.get("departure", ""),
        },
    )


@login_required
def get_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    form_passenger = PassengerForm(initial={"user": request.user})
    form_payment = PaymentForm()

    if request.method == "POST":
        form_passenger = PassengerForm(request.POST)
        form_payment = PaymentForm(request.POST)

        if form_passenger.is_valid() and form_payment.is_valid():
            passenger = form_passenger.save(commit=False)
            passenger.user = request.user
            passenger.save()

            ticket.passengers.add(passenger)
            ticket.quantity -= 1
            ticket.save()

            send_mail(
                "Ticket Purchase Confirmation",
                f"Thank you for your purchase. Your ticket details: Flight from {ticket.flight.origin} to {ticket.flight.destination}, Departure: {ticket.flight.departure}, Price: ${ticket.price}",
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email, passenger.email],
                fail_silently=False,
            )

            messages.success(
                request,
                "Your ticket has been purchased and a confirmation email has been sent.",
            )
            return redirect("main:profile")

    return render(
        request,
        "main/purchase.html",
        {
            "ticket": ticket,
            "form_passenger": form_passenger,
            "form_payment": form_payment,
        },
    )


class AllTicketsView(ListView):
    context_object_name = "tickets"
    model = Ticket
    template_name = "main/all_tickets.html"
    paginate_by = 6


@login_required
def profile(request):
    user_tickets = Ticket.objects.filter(passengers__user=request.user).distinct()
    if request.method == "POST":
        ticket_id = request.POST.get("ticket_id")
        passenger_id = request.POST.get("passenger_id")
        ticket = get_object_or_404(Ticket, id=ticket_id)
        passenger = get_object_or_404(Passenger, id=passenger_id)

        send_ticket_email.delay(ticket.id, passenger.email)
        messages.success(
            request, "The e-ticket has been sent to the passenger's email."
        )
        return redirect("main:profile")

    return render(
        request,
        "main/profile.html",
        {
            "user": request.user,
            "user_tickets": user_tickets,
            "default_image": settings.DEFAULT_PROFILE_IMAGE,
        },
    )


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")
