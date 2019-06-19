from django.db import models

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  notes = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"{self.first_name} {self.last_name}"

class Book(models.Model):
  title = models.CharField(max_length=255)
  authors = models.ManyToManyField(Author, related_name='books')
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"{self.title}"

