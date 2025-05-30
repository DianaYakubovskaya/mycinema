from django.contrib import admin
from .models import Movie, Show, CinemaHall

# Налаштування для моделі Movie
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_genres', 'release_date')  
    search_fields = ('title', 'genre__name')  
    list_filter = ('release_date',)  

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])  

# Налаштування для моделі Show
class ShowAdmin(admin.ModelAdmin):
    list_display = ('movie', 'show_time', 'get_cinema_hall')  
    search_fields = ('movie__title', 'cinema_hall__name')  
    list_filter = ('show_time',)  

    def get_cinema_hall(self, obj):
        return obj.cinema_hall.name  # Відображення назви залу
    get_cinema_hall.short_description = 'Зал'

# Реєстрація моделей з кастомними налаштуваннями
admin.site.register(Movie, MovieAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(CinemaHall)  
