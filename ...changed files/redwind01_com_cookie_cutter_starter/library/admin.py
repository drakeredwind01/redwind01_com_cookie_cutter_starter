from django.contrib import admin

# Register your models here.
from .models import Books


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Books._meta.fields]
    # or
    # fields = "__all__"
