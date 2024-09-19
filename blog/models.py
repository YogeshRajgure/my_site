from django.db import models
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
    
    caption = models.CharField( max_length=50)

    def __str__(self):
        return self.caption
    


class Author(models.Model):

    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Post(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    excerpt = models.TextField(max_length=500)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)
    tags = models.ManyToManyField(Tag, null=True)
    content = models.TextField(default="", null=True)


    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])
    
    def __str__(self):
        return self.title + f" ({self.date})"
    
