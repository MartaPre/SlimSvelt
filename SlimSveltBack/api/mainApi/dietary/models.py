from django.db import models

# Create your models here.
class Dietary(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  food_type = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  name = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  description = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )
  
  photo = models.ImageField(
    (""), 
    upload_to=None, 
    height_field=None, 
    width_field=None, 
    max_length=None
  )

  grams = models.DecimalField(
    (""), 
    max_digits=3, 
    decimal_places=2
  )

  kcal = models.DecimalField(
    (""), 
    max_digits=3, 
    decimal_places=2
  )

  class Meta:
    db_table = 'dietary'