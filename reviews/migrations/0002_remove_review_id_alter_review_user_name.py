# Generated by Django 5.1 on 2024-09-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="id",
        ),
        migrations.AlterField(
            model_name="review",
            name="user_name",
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
