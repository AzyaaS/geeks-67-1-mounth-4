from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)      
    image = models.ImageField(upload_to='book/' )
    year = models.IntegerField()  # год создания      
    pages = models.IntegerField()
    genre = models.CharField(max_length=50)
    age = models.IntegerField() # возрастное ограничение 
    url_blog = models.URLField(blank=True) # ссылка на литрес
    created_at = models.DateField(auto_now_add=True)  # Дата добавления
    

    def __str__(self):
        return self.title