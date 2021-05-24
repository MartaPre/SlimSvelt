from django.db import models
from users.models import Users
from recipes.models import Recipes


# Create your models here.
class RecipesUser(models.Model):
  id = models.AutoField(
    primary_key=True
  )
  user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_identificator')

  recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='recipes_identificator')

  kcal = models.DecimalField(
    (""), 
    max_digits=5, 
    decimal_places=2
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'recipes_user'