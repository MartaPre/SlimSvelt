from rest_framework import serializers

from .models import Recipes


class RecipesSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=1000, required=True)

  def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
    return Recipes.objects.create(
      name=validated_data.get('name')
    )

  def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
    instance.name = validated_data.get('name', instance.name)
    instance.save()
    return instance

  class Meta:
    model = Recipes
    fields = (
      'recipes_id',
      'name',
      'description',
      'recipe_type',
      'ingredients',
      'photo',
      'kcal'
    )