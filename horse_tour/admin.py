from django.contrib import admin
from . import models

admin.site.register(models.TourLocation)
admin.site.register(models.Horse)
admin.site.register(models.Review)
admin.site.register(models.HorseCategory)