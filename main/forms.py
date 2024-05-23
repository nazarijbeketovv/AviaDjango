# forms.py
from django import forms
from django.forms import widgets

from .models import Passenger


class FlightSearchForm(forms.Form):
    origin = forms.CharField(label="Origin", max_length=100)
    destination = forms.CharField(label="Destination", max_length=100)
    departure = forms.DateField(
        label="Departure", widget=forms.DateInput(attrs={"type": "date"})
    )


class PassengerForm(forms.ModelForm):

    class Meta:
        model = Passenger
        fields = ("full_name", "email", "passport_number")
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "passport_number": forms.TextInput(attrs={"class": "form-control"}),
        }


class PaymentForm(forms.Form):
    card_number = forms.CharField(
        label="Card Number",
        max_length=16,
        widget=forms.TextInput(attrs={"type": "number"}),
    )
    expiration_date = forms.DateField(
        label="Expiration Date",
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
    )
    cvv = forms.CharField(
        label="CVV",
        max_length=3,
        widget=forms.TextInput(attrs={"type": "number", "class": "form-control"}),
    )
