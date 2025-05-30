from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from cinema.models import Show

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Ticket(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='tickets_in_users_app')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tickets")
    seat_number = models.CharField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.show} - Seat {self.seat_number}"
