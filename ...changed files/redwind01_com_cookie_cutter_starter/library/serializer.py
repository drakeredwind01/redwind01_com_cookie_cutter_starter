from rest_framework import serializers
from library.models import Books


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ['author', 'book_title', 'checked_out_to', 'ratings', 'isbn']



