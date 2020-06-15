from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Employee
from .user import Users

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Employee
        url = serializers.HyperlinkedIdentityField(
            view_name='employee',
            lookup_field='id'
        )
        fields = ('id', 'city', 'phone', 'user_id', 'user')
        depth = 2

class Employees(ViewSet):

    def list(self, request):

        employee = Employee.objects.all()

        serializer = EmployeeSerializer(
        employee, many=True, context={'request': request}
        )

        return Response(serializer.data)

#     def create(self, request):

#         new_employee = Employee()

#         new_employee.city = request.data['city']
#         new_employee.phone = request.data['phone']

#         new