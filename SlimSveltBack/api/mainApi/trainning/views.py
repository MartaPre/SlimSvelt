from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Trainning
from .serializers import TrainningSerializer


class TrainningListView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def get(self, request, exercise_type=None, trainning_id=None):
    if trainning_id:
      # If an id is provided in the GET request, retrieve the Todo item by that id
      try:
        # Check if the todo item the user wants to update exists
        queryset = Trainning.objects.filter(trainning_id=trainning_id)
      except Trainning.DoesNotExist:
        # If the todo item does not exist, return an error response
        return Response({'errors': 'This trainning item does not exist.'}, status=400)

      # Serialize todo item from Django queryset object to JSON formatted data
      read_serializer = TrainningSerializer(queryset, many=True)
      
    elif exercise_type:
      # If an id is provided in the GET request, retrieve the Todo item by that id
      try:
        # Check if the todo item the user wants to update exists
        queryset = Trainning.objects.filter(exercise_type=exercise_type)
      except Trainning.DoesNotExist:
        # If the todo item does not exist, return an error response
        return Response({'errors': 'This trainning item does not exist.'}, status=400)

      # Serialize todo item from Django queryset object to JSON formatted data
      read_serializer = TrainningSerializer(queryset, many=True)
    
    

    else:
      # Get all todo items from the database using Django's model ORM
      queryset = Trainning.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
      read_serializer = TrainningSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
    return Response(read_serializer.data)


  def post(self, request):
    # Pass JSON data from user POST request to serializer for validation
    create_serializer = TrainningSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new todo item record in the database
      trainning_item_object = create_serializer.save()

      # Serialize the new todo item from a Python object to JSON format
      read_serializer = TrainningSerializer(trainning_item_object)

      # Return a HTTP response with the newly created todo item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)


  def put(self, request, id=None):
    try:
      # Check if the todo item the user wants to update exists
      trainning_item = Trainning.objects.get(id=id)
    except Trainning.DoesNotExist:
      # If the todo item does not exist, return an error response
      return Response({'errors': 'This trainning item does not exist.'}, status=400)

    # If the todo item does exists, use the serializer to validate the updated data
    update_serializer = TrainningSerializer(trainning_item, data=request.data)

    # If the data to update the todo item is valid, proceed to saving data to the database
    if update_serializer.is_valid():

      # Data was valid, update the todo item in the database
      trainning_item_object = update_serializer.save()

      # Serialize the todo item from Python object to JSON format
      read_serializer = TrainningSerializer(todo_item_object)

      # Return a HTTP response with the newly updated todo item
      return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
    return Response(update_serializer.errors, status=400)


  def delete(self, request, id=None):
    try:
      # Check if the todo item the user wants to update exists
      trainning_item = Trainning.objects.get(id=id)
    except Trainning.DoesNotExist:
      # If the todo item does not exist, return an error response
      return Response({'errors': 'This trainning item does not exist.'}, status=400)

    # Delete the chosen todo item from the database
    trainning_item.delete()

    # Return a HTTP response notifying that the todo item was successfully deleted
    return Response(status=204)