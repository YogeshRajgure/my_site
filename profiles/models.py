from django.db import models
import os

# Create your models here.

class UserProfile(models.Model):
    image = models.FileField(upload_to= os.path.join("profiles", "static", "profiles", "images") )