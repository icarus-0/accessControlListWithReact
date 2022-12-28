from rest_framework import serializers
from .models import *

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id','email','name','is_staff')

class RightGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RightGroups
        fields = "__all__"

class RightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rights
        fields = "__all__"

class UserRightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRights
        fields = "__all__"