from django.db import models

# MANY TO MANY
class HorseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ONE TO MANY 
class TourLocation(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название локации')
    address = models.CharField(max_length=200, verbose_name='Адрес локации')
    suitable_horse_types = models.ManyToManyField(HorseCategory)   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Локацию'
        verbose_name_plural = 'Локации'

# ONE TO ONE
class Horse(models.Model):
    name = models.CharField(max_length=50, verbose_name='Кличка лошади')
    location = models.OneToOneField(TourLocation, on_delete=models.CASCADE) 
    category = models.ForeignKey(HorseCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} - {self.location.title}'

# ONE TO MANY 
class Review(models.Model):
    location = models.ForeignKey(TourLocation, on_delete=models.CASCADE) 
    author = models.CharField(max_length=100, verbose_name='Имя пользователя')
    text = models.CharField(max_length=500, verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.location.title}'