from django.db import models
from django.conf import settings
from cinema.models import Show
import uuid

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='tickets_in_tickets_app')
    seat_number = models.CharField(max_length=10, default='A1')
    purchase_time = models.DateTimeField(auto_now_add=True)
    ticket_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @classmethod
    def available_seats(cls, show):
        return show.cinema_hall.capacity - cls.objects.filter(show=show).count()

    def __str__(self):
        return f'Ticket for {self.show.movie.title} - Seat: {self.seat_number} (User: {self.user.username if self.user else "Guest"})'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10, default='A1')

    def __str__(self):
        return f'Booking {self.id} by {self.user.username if self.user else "Guest"}'
