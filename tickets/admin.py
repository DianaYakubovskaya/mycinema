from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'show', 'seat_number', 'purchase_time')  # Оновлені правильні поля
    readonly_fields = ('purchase_time', 'ticket_uuid')  # Поля, які не можуть редагуватися
    list_filter = ('show__show_time', 'purchase_time')  # Додавання фільтра за часом сеансу та покупкою

admin.site.register(Ticket, TicketAdmin)




# Register your models here.
