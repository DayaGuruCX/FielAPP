from django import apps
from django.shortcuts import render
from pymongo import MongoClient
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reward
from .serializers import RewardSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from bson.objectid import ObjectId
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import generics
import json

client = MongoClient(settings.MONGODB_HOST)
db = client[settings.MONGODB_DB]


class RewardAPIView(APIView):   #otra forma de crear compañia
    def post(self, request, format=None):
        #URL = request.FILES['URL']
        data = request.body
        #datos_json = request.POST['datos']
        data=request.data
        data['company']=json.loads(request.POST['company'])
        serializer = RewardSerializer(data=request.data)

        try:
            if serializer.is_valid():
                print("4")
                
                reward = serializer.save()  # Guarda el objeto en la base de datos
                print("1")
                reward_id = reward.id  # Accede al ID del objeto creado
                print(reward_id)
                return Response({"message": "Premio creado", "reward_id": reward_id}, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Error:", str(e))


    @api_view(['GET','PUT'])
    def consult_reward(request, id):
    # Connect to the MongoDB database
        try:
            collection = db.Reward_reward
            #user = collection.find_one({'id': int(user_id)})
            if request.method=='PUT':
                # Get the user document with the provided ID
                #user = collection.find_one({'_id': user_id})
                if user is not None:
                    # Update the user document with the provided data
                    data = json.loads(request.body)
                    data['full_name']=request.data['name']+' '+request.data['last_name']
                    print(data['full_name'])
                    
                    collection.update_one({'id': int(user_id)}, {'$set': data})
                    partial_data = {
                        'id': user['id']
                    }

                    # Return a success response
                    return JsonResponse(partial_data, status=status.HTTP_200_OK) 
                else:
                    # Return an error response if the user is not found
                    return JsonResponse(data.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'GET':   
                reward = collection.find_one({'id': int(id)})
                partial_data = {
                    'url_premio': reward['URL'],
                    'costo_minimo': reward['minimun_cost'],
                    'Descriopcion': reward['description'],
                    'Punto para redimir': reward['redeem_points'],
                    'Fecha y hora de activación': reward['datetime_activate'],
                    'Tiene vencimiento': reward['has_expiration_date'],
                }
                return JsonResponse(partial_data, status=status.HTTP_200_OK) 
            
        except Exception as e:
            print("Error:", str(e))
