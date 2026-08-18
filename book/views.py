from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic  # ← НОВЫЙ ИМПОРТ
from django.core.paginator import Paginator
from .models import Book

class HelloWorldView(generic.View):
    def get(self, request):
        return HttpResponse('Hello World!')
class AboutView(generic.View):
    def get(self, request):
        return HttpResponse('Привет! Меня зовут Азирет, мне 23 года и я живу в Бишкеке')
class FavouriteGamesView(generic.View):
    def get(self, request):
        return HttpResponse('mobile legends')


class BookListView(generic.ListView):
    template_name = 'book_lst.html'
    model = Book
    paginate_by = 3
    ordering = ['-id']
    context_object_name = 'page_obj'

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'
    pk_url_kwarg = 'id'
    model = Book
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj