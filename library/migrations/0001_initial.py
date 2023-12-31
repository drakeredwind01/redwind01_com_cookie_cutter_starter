# Generated by Django 4.2.6 on 2023-10-15 04:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "author",
                    models.CharField(
                        default="default title", help_text="This is where you put your title", max_length=50
                    ),
                ),
                (
                    "book_title",
                    models.CharField(
                        default="default title", help_text="This is where you put your title", max_length=50
                    ),
                ),
                (
                    "checked_out_to",
                    models.CharField(
                        default="default title", help_text="This is where you put your title", max_length=50
                    ),
                ),
                (
                    "ratings",
                    models.PositiveSmallIntegerField(
                        default=100,
                        help_text="This is where you put a system for rating and reviewing the client and freelancer",
                    ),
                ),
                (
                    "isbn",
                    models.PositiveBigIntegerField(
                        default=100,
                        help_text="This is where you put a system for rating and reviewing the client and freelancer",
                    ),
                ),
            ],
        ),
    ]
