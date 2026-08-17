from django.urls import path
from . import views

urlpatterns = [
    path('create_order/', views.create_order_view),
    path('basket_list/', views.list_orders_view),
    path('basket_list/<int:id>/update/', views.update_order_view),
    path('basket_list/<int:id>/delete/', views.delete_order_view),
]