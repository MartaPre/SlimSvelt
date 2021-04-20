from django.db import models

# Create your models here.
class Users(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  user_type = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  name = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  email = models.EmailField(
    (""), 
    max_length=254
  )

  password = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  objective = models.TextField(
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

  weight = models.DecimalField(
    (""), 
    max_digits=3, 
    decimal_places=2
  )

  height = models.DecimalField(
    (""), 
    max_digits=3, 
    decimal_places=2
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  birth_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  last_updated = models.DateTimeField(
    auto_now=True,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'users'