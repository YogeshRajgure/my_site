# Generated by Django 5.1 on 2024-09-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_comments_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
