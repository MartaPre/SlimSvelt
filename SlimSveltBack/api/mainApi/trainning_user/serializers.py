from rest_framework import serializers

from .models import TrainningUser



class TrainningUserSerializer(serializers.ModelSerializer):
  # trainning_i = serializers.CharField(max_length=1000, required=True)
  # burned_kcal = serializers.DecimalField( required=True, max_digits=3, decimal_places=2)

  user_id= serializers.IntegerField()

  trainning_id = serializers.IntegerField()
  
  def create(self, validated_data):
    # Once the request data has been validated, we caFn create a todo item instance in the database
    return TrainningUser.objects.create(
      user_id=validated_data.get('user_id'),
      trainning_id=validated_data.get('trainning_id'),
      burned_kcal=validated_data.get('burned_kcal'),
    )

  def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
    instance.trainning_id = validated_data.get('user_id', instance.trainning_id)
    instance.save()
    return instance

  class Meta:
    model = TrainningUser
    fields = (
      'user_id',
      'trainning_id',
      'burned_kcal',
      'creation_date'
    )