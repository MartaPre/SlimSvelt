from django.db import models
from users.models import Users
from trainning.models import Trainning

# Create your models here.
class TrainningUser(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  user= models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users_identificator', null=True)

  trainning = models.ForeignKey(Trainning, on_delete=models.CASCADE, related_name='trainning_identificator', null=True)


  # user_id= models.IntegerField(source='users.users_id')

  # trainning_id = models.IntegerField(source='tranning.tranning_id')

  burned_kcal = models.DecimalField(
    (""), 
    null=True,
    max_digits=5, 
    decimal_places=2
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=True,
    blank=False
  )


  class Meta:
    db_table = 'trainning_user'