from django import forms
from .models import Ticket, Booking


class TicketBookingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['show', 'seat_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['show'].label = "Виберіть сеанс"
        self.fields['seat_number'].label = "Номер місця"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'show', 'seat_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].label = "Користувач"
        self.fields['show'].label = "Сеанс"
        self.fields['seat_number'].label = "Номер місця"
