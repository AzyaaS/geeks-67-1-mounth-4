from django.urls import path
from . import views

urlpatterns = [
    path('favourite/', views.my_favourite_book),
    path('about/', views.about_myself),
    path('games/', views.my_favourite_games),
]