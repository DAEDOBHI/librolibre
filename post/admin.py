from django.contrib import admin
from .models import *
# Register your models here.
#@admin.register(<nombre del modelo)
admin.site.register(Post)

admin.site.register(Country)

admin.site.register(Author)

class PostAdmin(admin.ModelAdmin):
    model = Post
    
class Author(admin.ModelAdmin):
    model = Author

class Country(admin.ModelAdmin):
    model = Country


