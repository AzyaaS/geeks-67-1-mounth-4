from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_favourite_book(request):
    if request.method == 'GET':
        return HttpResponse('Моя любимая книга - "Мартин Иден" Джек Лондон')

def about_myself(request):
    if request.method == 'GET':
        return HttpResponse('Привет! Меня зовут Азирет, мне 23 года и я живу в Бишкеке')

def my_favourite_games(request):
    if request.method == 'GET':
        return HttpResponse('mobile legends')
