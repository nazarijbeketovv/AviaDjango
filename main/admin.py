from django.contrib import admin
from .models import Airplane, Flight, Airline, Ticket, Flight, Passenger


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "email", "passport_number")

@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "origin",
        "destination",
        "departure",
        "arrival",
        "airline",
        "airplane",
    )


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("flight",)
