from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Books
from .serializer import BooksSerializer


# Create your views here.

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksTemplateView(TemplateView):
    template_name = "books.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books_list"] = Books.objects.all()
        return context
