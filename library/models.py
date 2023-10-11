from django.db import models
from django.db.models import CharField, PositiveSmallIntegerField
# Create your models here.

# 123
class Books(models.Model):
    author = models.CharField(max_length=50, default="default title", help_text="This is where you put your title", )
    book_title = models.CharField(max_length=50, default="default title", help_text="This is where you put your title", )
    checked_out_to = models.CharField(max_length=50, default="default title", help_text="This is where you put your title", )
    ratings = models.PositiveSmallIntegerField(default=100, help_text="This is where you put a system for rating and reviewing the client and freelancer", )
    isbn = models.PositiveBigIntegerField(default=100, help_text="This is where you put a system for rating and reviewing the client and freelancer", )
# PositiveSmallIntegerField = 0 to 32767
# PositiveIntegerField      = 0 to 2147483647
# PositiveBigIntegerField   = 0 to 9223372036854775807
# ISBN                      =      1097814218062420


