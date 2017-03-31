from django.core.context_processors import csrf
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse


def index(request):
    return render(request, 'loginsys/login.html', {'question': 1})

def login(request):
    if request.POST:
        print("ololo")
    print(request)
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return redirect('/xo')
    else:
        # Отображение страницы с ошибкой
        return HttpResponse("Error auth")

def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return redirect("/loginsys/")