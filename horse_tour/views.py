from django.shortcuts import render
from . import models

def locations_list_view(request):
    if request.method == 'GET':
        locations = models.TourLocation.objects.all()
    return render(request, 'horse_tour_list.html', {'locations': locations})