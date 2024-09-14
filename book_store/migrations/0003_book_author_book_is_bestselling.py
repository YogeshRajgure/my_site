# Generated by Django 5.1 on 2024-09-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_store", "0002_alter_book_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="is_bestselling",
            field=models.BooleanField(default=False),
        ),
    ]
