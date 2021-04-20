from django.db import models

# Create your models here.
class TrainningDiary(models.Model):
  id = models.AutoField(
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

  burned_kcal = models.DecimalField(
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
    db_table = 'trainning_diary'