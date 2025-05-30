from django.urls import path
from . import views

urlpatterns = [
    path('select_seat/<int:show_id>/', views.select_seat, name='select_seat'),
    path('confirm_booking/<int:booking_id>/', views.confirm_booking, name='confirm_booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('ticket_booking/<int:show_id>/', views.ticket_booking, name='ticket_booking'),
]
