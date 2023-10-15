from django.db import models
from django.db.models import CharField, PositiveSmallIntegerField
from django.conf import settings
from django.db.models import ForeignKey
from django.db.models import DO_NOTHING
# Create your models here.

# 123
class Books(models.Model):
    book_title = models.CharField(max_length=50, default="default title", help_text="This is where you put your title", )
    author = models.CharField(max_length=50, default="default title", help_text="This is where you put your title", )
    isbn = models.PositiveBigIntegerField(default=100, help_text="This is where you put a system for rating and reviewing the client and freelancer", )
    ratings = models.PositiveSmallIntegerField(default=100, help_text="This is where you put a system for rating and reviewing the client and freelancer", )
    checked_out_to = models.CharField(max_length=50, default="default title", help_text="This is where you put your title", )
    checked_out_to2 = ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=DO_NOTHING)


# PositiveSmallIntegerField = 0 to 32767
# PositiveIntegerField      = 0 to 2147483647
# PositiveBigIntegerField   = 0 to 9223372036854775807
# ISBN                      =      9781421806242


