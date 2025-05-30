from django.urls import path
from django.contrib.auth import views as auth_views  
from .views import login_view, register_view, profile_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
    
]
