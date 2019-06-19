from django.db import models

class Author(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  notes = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __repr__(self):
    return f"{self.first_name} {self.last_name}"

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=255)
  authors = models.ManyToManyField(Author, related_name="books")
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"{self.title} {self.author}"
