from django.db import models

# Create your models here.
class Trainning(models.Model):
  trainning_id = models.AutoField(
    primary_key=True
  )

  exercise_type = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  name = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  intensity = models.TextField(
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

  burned_kcal = models.DecimalField(
    (""), 
    max_digits=3, 
    decimal_places=2
  )

  class Meta:
    db_table = 'trainning'