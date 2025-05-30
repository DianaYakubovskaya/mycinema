from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm 


# Вхід користувача
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Ласкаво просимо назад, {}'.format(user.username))  
            return redirect('profile')  # Перенаправлення на профіль користувача
        else:
            messages.error(request, 'Неправильне ім\'я користувача або пароль.')
    return render(request, 'users/login.html')  # Відображення сторінки входу

# Сторінка профілю доступна лише для авторизованих користувачів
@login_required
def profile_view(request):
    tickets = request.user.tickets.all()  

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профіль успішно оновлено.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {
        'tickets': tickets,
        'form': form
    })


# Реєстрація нового користувача
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматичний вхід після реєстрації
            messages.success(request, 'Реєстрація успішна! Ласкаво просимо, {}'.format(user.username))
            return redirect('profile')  # Перенаправлення на профіль користувача
        else:
            messages.error(request, 'Будь ласка, виправте помилки нижче.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})  # Відображення сторінки реєстрації
