from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
  
  def basic_validator(self, postData):
    errors = {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    if len(postData['first_name']) < 2:
      errors['first_name'] = 'First name must have at least two characters'
    if not EMAIL_REGEX.match(postData['email']):
      errors['email'] = 'Email needs to be in the correct format'
    if len(postData['last_name']) < 2:
      errors['last_name'] = 'Last name must have at least two characters'
    if len(postData['password']) < 8:
      errors['password'] = 'Password must be at least eight characters long'
    if postData['password'] != postData['confirm']:
      errors['confirm'] = 'Confirm password does not match password'
    return errors

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()

  def __repr__(self):
    return f'{self.first_name} {self.last_name}'



# class Movie(models.Model):
#   title = models.CharField(max_length=45)
#   description = models.TextField()
#   release_date = models.DateTimeField()
#   duration = models.IntegerField()
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
