from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game


def home(request):
    return render(request, 'fourth_task/home.html')


def shop(request):
    games = Game.objects.all()

    return render(request, 'fourth_task/shop.html', {
        'games': games
    })


def cart(request):
    return render(request, 'fourth_task/cart.html')


def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST or None)

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        repeat_password = form.cleaned_data["repeat_password"]
        age = form.cleaned_data["age"]

        # Проверка паролей и возраста
        if password != repeat_password:
            info["error"] = "Пароли не совпадают"
        elif int(age) < 18:
            info["error"] = "Вы должны быть старше 18"
        elif Buyer.objects.filter(name=name).exists():
            info["error"] = "Пользователь с таким именем уже существует"
        else:
            # Добавляем нового пользователя в базу данных
            Buyer.objects.create(name=name, balance=0.0, age=age)
            return HttpResponse(f"Приветствуем, {name}!")

    info["form"] = form
    return render(request, "fifth_task/registration_page.html", info)


def sign_up_by_html(request):
    info = {}

    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        # Проверка паролей и возраста
        if password != repeat_password:
            info["error"] = "Пароли не совпадают"
        elif int(age) < 18:
            info["error"] = "Вы должны быть старше 18"
        elif Buyer.objects.filter(name=name).exists():
            info["error"] = "Пользователь с таким именем уже существует"
        else:
            # Добавляем нового пользователя в базу данных
            Buyer.objects.create(name=name, balance=0.0, age=age)
            return HttpResponse(f"Приветствуем, {name}!")

    return render(request, "fifth_task/registration_page.html", info)
