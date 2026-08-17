from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

# CREATE
def create_order_view(request):
    if request.method == 'POST':
        form_obj = forms.BasketForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/basket_list/')
    else:
        form_obj = forms.BasketForm()
    return render(request, 'create_order.html', {'form': form_obj})

# READ
def list_orders_view(request):
    if request.method == 'GET':
        orders_list = models.BasketBook.objects.all()
    return render(request, 'list_orders.html', {'orders_list': orders_list})

# UPDATE
def update_order_view(request, id):
    order_id = get_object_or_404(models.BasketBook, id=id)
    if request.method == 'POST':
        form_obj = forms.BasketForm(request.POST, instance=order_id)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/basket_list/')
    else:
        form_obj = forms.BasketForm(instance=order_id)
    return render(request, 'update_order.html', {'form': form_obj, 'order_id': order_id})

# DELETE
def delete_order_view(request, id):
    order_id = get_object_or_404(models.BasketBook, id=id)
    order_id.delete()
    return redirect('/basket_list/')