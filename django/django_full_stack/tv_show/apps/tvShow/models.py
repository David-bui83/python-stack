from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    d = datetime.now()

    if len(postData['title']) < 2:
      errors['title'] = 'Title must be at least two characters'
    if len(postData['network']) < 3:
      errors['network'] = 'Network needs to be at least 3 characters'
    if len(postData['desc']) > 1 and len(postData['desc']) < 10:
      errors['desc'] = 'Description can be blank or must be at least 10 characters'
    if datetime.strptime(postData['date'],'%Y-%m-%d') > d:
      errors['date'] = 'Release date cannot be greater than current date'
    
    return errors

# Create your models here.
class Show(models.Model):
  title = models.CharField(max_length=255)
  network = models.CharField(max_length=255)
  release_date = models.DateTimeField()
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ShowManager()

  def __repr__(self):
    return f"{self.title}"

# class BlogManager(models.Manager):
#   def basic_validator(self, postData):
#       errors = {}
#       # add keys and values to errors dictionary for each invalid field
#       if len(postData['name']) < 5:
#           errors["name"] = "Blog name should be at least 5 characters"
#       if len(postData['desc']) < 10:
#           errors["desc"] = "Blog description should be at least 10 characters"copy
#       return errors

# class Blog(models.Model):
#   name = models.CharField(max_length=255)
#   desc = models.TextField()
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
#   objects = BlogManager()    # add this line!