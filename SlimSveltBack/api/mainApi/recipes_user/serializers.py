from rest_framework import serializers

from .models import RecipesUser


class RecipesUserSerializer(serializers.ModelSerializer):
  user_id= serializers.IntegerField()

  recipes_id = serializers.IntegerField()
  def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database

    return RecipesUser.objects.create(
      user_id=validated_data.get('user_id'),
      recipes_id=validated_data.get('recipes_id'),
      grams=validated_data.get('grams'),
    )

  def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
    instance.name = validated_data.get('name', instance.name)
    instance.save()
    return instance

  class Meta:
    model = RecipesUser
    fields = (
      'user_id',
      'recipes_id',
      'grams',
      'creation_date'
    )