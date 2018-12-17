from django.test import TestCase
from .models import Image, Profile
import datetime as dt

class ImageTestClass(TestCase):
  
  def setUp(self):
    self.master = Profile(user='Jeremy', bio='Hello')

    self.image = Image(image_name='Test Name', image_caption='Test Caption', profile=self.master)

  def tearDown(self):
    Profile.delete_profile()
    Image.delete_image()

  def test_instance(self):
    self.assertTrue(isinstance(self.image, Image))

  def test_save_instance(self):
    self.image.save_image()
    images = Image.get_images()
    self.assertTrue(len(images)>0)

  def test_delete_instance(self):
    self.image.save_image()
    self.image.delete_image()
    images = Image.get_images()
    self.assertTrue(len(images) == 0)

class ProfileTestClass(TestCase):

  def setUp(self):
    self.master = Profile(user='Jeremy', bio='Hello')

  def tearDown(self):
    Profile.delete_profile()

  def test_instance(self):
    self.assertTrue(isinstance(self.master, Master))

  def test_save_instance(self):
    self.master.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles)>0)

  def test_delete_instance(self):
    self.profile.save_profile()
    self.profile.delete_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) == 0)
