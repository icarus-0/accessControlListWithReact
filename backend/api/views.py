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
        name = request.POST['name']
        password =  request.POST['password']
        db = get_user_model()
        
        try:
            user = db.objects.create_user(email=email,name=name,password=password)
            res = dict()
            res['id'] = user.id
            res['email'] = user.email
            res['name'] = user.name
            res['status'] = 200
        except Exception as e:
            res = dict()
            res['id'] = None
            res['email'] = email
            res['name'] = name
            res['status'] = 500
            res['error'] = str(e)
        return JsonResponse(res,safe=False)

class RightGroupsList(APIView):

    def get(self,request):
        groups = RightGroups.objects.all()
        serializer = RightGroupsSerializer(groups,many=True)
        return Response(serializer.data)

    def post(self,request):
        try:
            name = request.POST['name']
            ins = RightGroups(name=name)
            ins.save()
            res = {
                'id':ins.id,
                'name' : name,
                'status' : 200,
            }
            return JsonResponse(res)
        except Exception as e:
            res = {
                'status' : 500,
                'error' : str(e)
            }
            return JsonResponse(res)
    
    def put(self,request):
        try:
            types = request.POST['type']
            id = request.POST['id']
            ins = RightGroups.objects.filter(id=id)

            if len(ins) == 1:
                ins = ins[0]
                if types == 'inactivate':
                    ins.is_active = False
                    ins.save()
                    res = {
                        'status' : 200,
                        'message' : 'Right Group Inactivated'
                    }
                elif types == 'activate':
                    ins.is_active = True
                    ins.save()
                    res = {
                        'status' : 200,
                        'message' : 'Right Group Activated'
                    }
                else:
                    res = {
                        'status' : 400,
                        'message' : 'Bad Request Type'
                    }
            else:
                res = {
                    'status' : 404,
                    'error' : 'No Right Group Exist With Given Id'
                }
            
            return JsonResponse(res)
        except Exception as e:
            res = {
                    'status' : 500,
                    'error' : str(e)
                }
            return JsonResponse(res)
    
    def delete(self,request):
        try:
            id = request.POST['id']
            ins = RightGroups.objects.filter(id=id)
            if len(ins) == 1:
                ins = ins[0]
                ins.delete()
                res = {
                    'status' : 200,
                    'message' : 'Right Group Deleted Successfully'
                }
            else:
                res = {
                    'status' : 404,
                    'error' : 'No Right Group Present With Given Id'
                }
            return JsonResponse(res)
        except Exception as e:
            res = {
                    'status' : 500,
                    'error' : str(e)
                }
            return JsonResponse(res)
        
class RightsList(APIView):

    def get(self,request):
        rights = Rights.objects.all()
        serializer = RightsSerializer(rights,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        try:
            name = request.POST['name']
            group_id =  request.POST['groupid']
            group_ins = RightGroups.objects.filter(id=group_id)
            if len(group_ins) == 1:
                group_ins = group_ins[0]
                if group_ins.is_active == True:
                    right_ins = Rights(name=name,right_group=group_ins)
                    right_ins.save()
                    res = {
                        'status' : 200,
                        'id' : right_ins.id,
                        'name' : name,
                        'message' : 'Right successfully created'
                    }
                else:
                    res = {
                        'status' : 403,
                        'error' : 'Right Group is inactive'
                    }
            else:
                res = {
                    'status' : 404,
                    'error' : 'Given Right Group is not present'
                }
            return JsonResponse(res)
        except Exception as e:
            res = {
                'status' : 500,
                'error' : str(e)
            }
            return JsonResponse(res)
    
    def put(self,request):
        try:
            types = request.POST['type']
            id = request.POST['id']
            ins = Rights.objects.filter(id=id)

            if len(ins) == 1:
                ins = ins[0]
                if types == 'inactivate':
                    ins.is_active = False
                    ins.save()
                    res = {
                        'status' : 200,
                        'message' : 'Right Inactivated'
                    }
                elif types == 'activate':
                    ins.is_active = True
                    ins.save()
                    res = {
                        'status' : 200,
                        'message' : 'Right Activated'
                    }
                else:
                    res = {
                        'status' : 400,
                        'message' : 'Bad Request Type'
                    }
            else:
                res = {
                    'status' : 404,
                    'error' : 'No Right Exist With Given Id'
                }
            
            return JsonResponse(res)
        except Exception as e:
            res = {
                    'status' : 500,
                    'error' : str(e)
                }
            return JsonResponse(res)
    
    def delete(self,request):
        try:
            id = request.POST['id']
            ins = Rights.objects.filter(id=id)
            if len(ins) == 1:
                ins = ins[0]
                ins.delete()
                res = {
                    'status' : 200,
                    'message' : 'Right Deleted Successfully'
                }
            else:
                res = {
                    'status' : 404,
                    'error' : 'No Right Present With Given Id'
                }
            return JsonResponse(res)
        except Exception as e:
            res = {
                    'status' : 500,
                    'error' : str(e)
                }
            return JsonResponse(res)




