from django.db import models
import datetime as dt
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(default='Single and ready to mingle', max_length=500, blank=True)
  photo = models.ImageField(blank=True, upload_to='photos/')

  def __str__(self):
    return self.user

class Image(models.Model):
  image = models.ImageField(upload_to='photos/')
  image_name = models.CharField(max_length = 60)
  image_caption = models.CharField(max_length = 60)
  posted_at = models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

