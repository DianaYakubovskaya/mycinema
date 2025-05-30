from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Movie, Show
from datetime import datetime


# Список фільмів з пагінацією
def movie_list(request):
    sort_by = request.GET.get('sort', 'popularity')  # отримуємо параметр сортування з URL

    # Сортування фільмів
    if sort_by == 'novelty':
        movies = Movie.objects.filter(active=True).order_by('-release_date')
    elif sort_by == 'rating':
        movies = Movie.objects.filter(active=True).order_by('-imdb_rating')
    else:
        movies = Movie.objects.filter(active=True).order_by('-total_tickets_sold')

    paginator = Paginator(movies, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'cinema/movie_list.html', {'page_obj': page_obj, 'sort_by': sort_by})

# Деталі конкретного фільму
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'cinema/movie_detail.html', {'movie': movie})

# Розклад сеансів з пагінацією
def schedule(request):
    selected_date = request.GET.get('date', datetime.today().date())  # за замовчуванням поточна дата
    shows = Show.objects.filter(show_time__date=selected_date)

    paginator = Paginator(shows, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'cinema/schedule.html', {'page_obj': page_obj, 'selected_date': selected_date})

# Бронювання квитка на конкретний сеанс
def ticket_booking(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    return render(request, 'cinema/ticket_booking.html', {'show': show})
