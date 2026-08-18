from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)      
    image = models.ImageField(upload_to='book/')
    year = models.IntegerField()
    pages = models.IntegerField()
    genre = models.CharField(max_length=50)
    age = models.IntegerField()
    url_blog = models.URLField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.title