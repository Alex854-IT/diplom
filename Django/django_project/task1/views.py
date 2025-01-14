from django.shortcuts import render
from .forms import UserRegister
from django.db import models
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def plat(request):
    return render(request, "platform.html")

# def games(request):
#     context = {
#         'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
#     }
#     return render(request, "games.html", context)  #  Имя шаблона для методов (функций)

def games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})

def cart(request):
    return render(request, "cart.html")

def menu(request):
    return render(request, "menu.html")


def sign_up_by_django(request):
    info = {}
    buyers = Buyer.objects.all()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']


            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            # elif any(buyer.name == username for buyer in buyers):
            #     info['error'] = 'Пользователь уже существует'
            elif username in buyers:
                info['error'] = 'Пользователь уже существует'

            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                return render(request, 'registration_page.html', {'message': f'Приветствуем, {username}!'})
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    buyers = Buyer.objects.all()
    if request.method == 'POST':
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif any(buyer.name == username for buyer in buyers):
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                return render(request, 'registration_page.html', {'message': f'Приветствуем, {username}!'})


    return render(request, 'registration_page.html', info)


def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'news': page_obj}

    return render(request, 'news.html', context)
