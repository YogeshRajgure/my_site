# Generated by Django 5.1 on 2024-09-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_store", "0003_book_author_book_is_bestselling"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
