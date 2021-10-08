from django.contrib import admin
from .models import Books, Rental

class BooksAdmin(admin.ModelAdmin):
    search_fields = ['title','Writer']


admin.site.register(Books, BooksAdmin)
admin.site.register(Rental)