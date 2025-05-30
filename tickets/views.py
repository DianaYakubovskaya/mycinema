from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from cinema.models import Show
from django.contrib import messages
from .forms import TicketBookingForm  

def select_seat(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    
    # Перевірка, чи користувач автентифікований
    if not request.user.is_authenticated:
        return redirect('login')  # Перенаправлення на сторінку входу

    # Отримуємо список заброньованих місць
    booked_seats = Booking.objects.filter(show=show).values_list('seat_number', flat=True)

    if request.method == 'POST':
        selected_seats = request.POST.getlist('selected_seats')  # Отримуємо всі вибрані місця

        # Створюємо бронювання для кожного вибраного місця
        for seat_number in selected_seats:
            if int(seat_number) not in booked_seats:  # Перевіряємо, чи не заброньоване місце
                booking = Booking.objects.create(user=request.user, show=show, seat_number=seat_number)
                booking.save()

        messages.success(request, 'Ваші місця успішно заброньовані!')
        return redirect('my_bookings')  # Перенаправлення на сторінку з бронюваннями

    return render(request, 'tickets/select_seat.html', {'show': show, 'booked_seats': booked_seats})

def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'tickets/confirm_booking.html', {'booking': booking})

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'tickets/my_bookings.html', {'bookings': bookings})

def book_ticket_view(request):
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            form.save()  # Збережіть квиток
            messages.success(request, 'Ваш квиток успішно заброньовано!')
            return redirect('movie_list')  # Перенаправлення на сторінку зі списком фільмів
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = TicketBookingForm()

    return render(request, 'tickets/book_ticket.html', {'form': form})

def ticket_booking(request, show_id):
    show = get_object_or_404(Show, id=show_id)

    # Генеруємо список номерів місць
    seat_numbers = range(1, show.cinema_hall.capacity + 1)  # Використання capacity з cinema_hall

    # Отримуємо заброньовані місця для даного показу
    booked_seats = Booking.objects.filter(show=show).values_list('seat_number', flat=True)

    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            form.save()  # Збереження бронювання
            messages.success(request, 'Ваш квиток успішно заброньовано!')
            return redirect('movie_list')  # Перенаправлення після успішного бронювання
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = TicketBookingForm()  # Відображення порожньої форми

    return render(request, 'cinema/ticket_booking.html', {
        'form': form,
        'show': show,
        'seat_numbers': seat_numbers,  # Передаємо список місць в шаблон
        'booked_seats': booked_seats
    })





# Create your views here.
