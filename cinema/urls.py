from django.urls import path
from .views import movie_list, movie_detail, schedule, ticket_booking
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', movie_list, name='movie_list'),  # Головна сторінка з фільмами
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),  # Сторінка конкретного фільму
    path('schedule/', schedule, name='schedule'),  # Сторінка розкладу сеансів
    path('ticket_booking/<int:show_id>/', ticket_booking, name='ticket_booking'),  # Бронювання квитка на сеанс
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
