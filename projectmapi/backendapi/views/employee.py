from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = EmployeetModel
        url = serializers.HyperlinkedIdentityField(
            view_name='employee',
            lookup_field='id'
        )
        fields = ('id', 'city', 'phone', 'user')
        depth = 1

class Employee(ViewSet):

    def create(self, request):

        new_employee =