from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

def book_list_view(request):
    if request.method == 'GET':
        books_lst = Book.objects.all().order_by('-id')
    return render(request, 'book_lst.html', {'books_lst': books_lst})

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book_id': book_id})



def my_favourite_book(request):
    if request.method == 'GET':
        return HttpResponse('Моя любимая книга - "Мартин Иден" Джек Лондон')

def about_myself(request):
    if request.method == 'GET':
        return HttpResponse('Привет! Меня зовут Азирет, мне 23 года и я живу в Бишкеке')

def my_favourite_games(request):
    if request.method == 'GET':
        return HttpResponse('mobile legends')
