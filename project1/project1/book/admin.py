from django.contrib import admin
from .models import books
# Register your models here.
class booksAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['id']

admin.site.register(books, booksAdmin)