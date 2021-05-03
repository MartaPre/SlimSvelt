from django.db import models

# Create your models here.
class Ingredients(models.Model):
  ingredients_id = models.AutoField(
    primary_key=True
  )

  ingredient_type = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  name = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  kcal = models.DecimalField(
    (""), 
    max_digits=3, 
    decimal_places=2
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )


  class Meta:
    db_table = 'ingredients'