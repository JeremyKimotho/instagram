from django.db import models
import datetime as dt
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(default='Single and ready to mingle', max_length=500, blank=True)
  photo = models.ImageField(blank=True, upload_to='photos/')

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()

  def update_profile(self, id, updated_bio):
    profile = Profile.objects.filter(pk=id).update(bio = updated_bio)
    return profile.save_profile()

  @classmethod
  def search_profile(cls, search):
    profile = cls.objects.filter(user__username__icontains=search)
    return profile

  def __str__(self):
    return self.user.username

class Image(models.Model):
  image = models.ImageField(blank=True, upload_to='photos/')
  image_name = models.CharField(max_length = 60)
  image_caption = models.CharField(max_length = 60)
  posted_at = models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  def update_profile(self, id, updated_caption):
    image = Image.objects.filter(pk=id).update(image_caption = updated_caption)
    return image.save_image()

  @classmethod
  def get_images(cls):
    images = cls.objects.all()
    return images

  def __str__(self):
    return self.image.url


