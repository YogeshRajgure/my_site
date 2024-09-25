from django.db import models

# Create your models here.


class Review(models.Model):
    user_name = models.CharField( max_length=100, primary_key=True)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.user_name + "    " + f"({self.rating})"

