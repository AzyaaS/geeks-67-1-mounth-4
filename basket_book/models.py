from django.db import models
from book.models import Book

class BasketBook(models.Model):
    name_order = models.CharField(max_length=100, verbose_name='ФИО')
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество')
    card = models.CharField(max_length=16, verbose_name='Номер карты')
    status = models.CharField(max_length=20, default='В обработке', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name_order} - {self.choice_book.title}'
