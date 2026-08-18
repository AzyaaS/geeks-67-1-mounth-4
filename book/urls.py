from django.urls import path
from . import views

urlpatterns = [
    path('favourite/', views.HelloWorldView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('games/', views.FavouriteGamesView.as_view()),
    path('', views.BookListView.as_view(), name='book_list'),
    path('book_list/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
]