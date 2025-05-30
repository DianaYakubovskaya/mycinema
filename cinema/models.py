from django.db import models
import uuid

class Poster(models.Model):
    image = models.ImageField(upload_to='posters/')

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(upload_to='posters/')
    trailer_url = models.URLField()
    release_date = models.DateField()
    duration = models.DurationField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_3d = models.BooleanField(default=False)
    age_restriction = models.PositiveSmallIntegerField()
    movie_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    imdb_rating = models.FloatField(default=0.0, null=False)
    total_tickets_sold = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='shows')
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, related_name='shows')
    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} at {self.show_time}"

    @property
    def available_seats(self):
        from tickets.models import Booking
        booked_seats_count = Booking.objects.filter(show=self).count()
        return self.cinema_hall.capacity - booked_seats_count
