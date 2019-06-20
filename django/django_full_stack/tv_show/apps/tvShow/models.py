from django.db import models

# Create your models here.
class Show(models.Model):
  title = models.CharField(max_length=255)
  network = models.CharField(max_length=255)
  release_date = models.DateTimeField()
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"{self.title}"

# class Movie(models.Model):
#   title = models.CharField(max_length=45)
#   description = models.TextField()
#   release_date = models.DateTimeField()
#   duration = models.IntegerField()
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)