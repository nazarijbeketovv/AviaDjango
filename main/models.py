from django.db import models
from django.contrib.auth import get_user_model


class Airplane(models.Model):
    """
    Модель самолета.

    Атрибуты:
        name (CharField): Название самолета.
        seats (PositiveIntegerField): Количество мест в самолете.
    """

    name = models.CharField(max_length=64)
    seats = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name


class Airline(models.Model):
    """
    Модель авиакомпании.

    Атрибуты:
        name (CharField): Название авиакомпании.
    """

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Flight(models.Model):
    """
    Модель рейса.

    Атрибуты:
        origin (CharField): Город отправления.
        destination (CharField): Город назначения.
        departure (DateTimeField): Время отправления.
        arrival (DateTimeField): Время прибытия.
        airline (ForeignKey): Связь с моделью Airline.
        airplane (ForeignKey): Связь с моделью Airplane.
    """

    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    airline = models.ForeignKey("Airline", on_delete=models.CASCADE)
    airplane = models.ForeignKey("Airplane", on_delete=models.CASCADE)

    def get_duration(self):
        """
        Возвращает длительность рейса в формате 'X days, Y hours, Z minutes'.
        """
        duration = self.arrival - self.departure
        days, seconds = duration.days, duration.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{days} days, {hours} hours, {minutes} minutes"

    def __str__(self):
        return f"{self.origin} -> {self.destination}"


class Passenger(models.Model):
    """
    Модель пассажира.

    Атрибуты:
        user (ForeignKey): Связь с моделью пользователя.
        full_name (CharField): Полное имя пассажира.
        email (EmailField): Email пассажира.
        passport_number (CharField): Номер паспорта пассажира.
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    passport_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name} - {self.email}"


class Ticket(models.Model):
    """
    Модель билета.

    Атрибуты:
        flight (ForeignKey): Связь с моделью рейса.
        price (PositiveIntegerField): Цена билета.
        class_type (CharField): Класс билета (economy, business, first).
        users_who_bought (ManyToManyField): Пользователи, купившие билет.
        passengers (ManyToManyField): Пассажиры, связанные с билетом.
        quantity (PositiveIntegerField): Количество билетов.
    """

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
