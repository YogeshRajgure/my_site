# Generated by Django 5.1 on 2024-09-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_author_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image_name",
            field=models.ImageField(upload_to="uploads\\posts"),
        ),
    ]
