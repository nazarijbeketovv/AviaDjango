from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("all_tickets/", views.AllTicketsView.as_view(), name="all_tickets"),
    path("profile/", views.profile, name="profile"),
    path("get_ticket/<int:pk>/", views.get_ticket, name="get_ticket"),
    path("search/", views.search_flights, name="search_flights"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
