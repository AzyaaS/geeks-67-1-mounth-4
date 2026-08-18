from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator 
from .models import Book

def book_list_view(request):
    if request.method == 'GET':
        books_lst = Book.objects.all().order_by('-id')
        search_query = request.GET.get('search')
        if search_query:
            books_lst = books_lst.filter(title__icontains=search_query)
        paginator = Paginator(books_lst, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
    return render(request, 'book_lst.html', {'page_obj': page_obj, 'search_query': search_query})

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book, id=id)
        book_id.views += 1
        book_id.save()
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