from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, blank=False)
    content = models.CharField(max_length=500, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    pages = models.PositiveIntegerField(default = 0)
    author = models.ForeignKey(
        'Author', 
        on_delete = models.PROTECT, 
        related_name='books',
        null = True,
        )
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=144)
    biography = models.CharField(max_length = 1000)
    country = models.ForeignKey('Country', on_delete= models.PROTECT, related_name= 'authors', null = True, blank = True)
    def __str__(self):
        return self.name
        
class Country(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name