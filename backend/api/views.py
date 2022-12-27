from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from django.contrib.auth import get_user_model
import json

class UserAccountList(APIView):

    def get(self,request):
        accounts = UserAccount.objects.all()
        serializer = UserAccountSerializer(accounts,many=True)
        return Response(serializer.data)

    def post(self,request):
        email = request.POST['email']
        name = request.POSt['name']
        password =  request.POST['password']
        types = request.POST['type']

        if types == 'user':
            db = get_user_model()

            try:
                user = db.objects.create_user(email=email,name=name,password=password)
                
                res = {
                    'id':user.id,
                    'email':user.email,
                    'name':user.name,
                    'status': 200
                }
                
            except Exception as e:
                res = {
                    'id':None,
                    'email':email,
                    'name':name,
                    'status': 500,
                    'error': str(e)
                }
            res = json.dumps(res)
            return JsonResponse(res)
        else:
            res = {
                    'id':None,
                    'email':None,
                    'name':None,
                    'status': 500,
                    'error': str(e)
                }
            res = json.dumps(res)
            return JsonResponse(res)
        


