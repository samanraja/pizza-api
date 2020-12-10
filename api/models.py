from django.db import models

# Create your models here.

class Task(models.Model):
  typee = models.CharField(max_length=200)
  size = models.CharField(max_length=200, default=False)
  topping = models.CharField(max_length=200, default=False)
  
      
  def __str__(self):
    return self.typee