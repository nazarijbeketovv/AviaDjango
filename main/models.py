from django.db import models
from django.contrib.auth import get_user_model


class Airplane(models.Model):
    name = models.CharField(max_length=64)
    seats = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name


class Airline(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    airline = models.ForeignKey("Airline", on_delete=models.CASCADE)
    airplane = models.ForeignKey("Airplane", on_delete=models.CASCADE)

    def get_duration(self):
        duration = self.arrival - self.departure
        days, seconds = duration.days, duration.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{days} days, {hours} hours, {minutes} minutes"

    def __str__(self):
        return f"{self.origin} -> {self.destination}"


class Passenger(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    passport_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name} - {self.email}"


class Ticket(models.Model):
    CLASS_TYPE_CHOICES = [
        ("economy", "Economy"),
        ("business", "Business"),
        ("first", "First Class"),
    ]

    flight = models.ForeignKey("Flight", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    class_type = models.CharField(
        max_length=20, choices=CLASS_TYPE_CHOICES, default="economy"
    )
    users_who_bought = models.ManyToManyField(
        get_user_model(), related_name="tickets", blank=True
    )
    passengers = models.ManyToManyField("Passenger", related_name="tickets", blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.flight}"
