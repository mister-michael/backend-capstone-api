from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Employee
from .user import Users
from django.contrib.auth.models import User

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

    def update(self, request, pk=None):

        employee = Employee.objects.get(user_id=request.auth.user.id)

        employee.city = request.data['city']
        employee.phone = request.data['phone']

        user_to_update = User.objects.get(pk=request.auth.user.id)

        user_to_update.email = request.data['email']
        user_to_update.first_name = request.data['first_name']
        user_to_update.last_name = request.data['last_name']

        employee.save()
        user_to_update.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(
                employee, context={'request': request}
                )
            return Response(serializer.data)

        except Exception as ex:
            
            return HttpResponseServerError(ex)


#     def create(self, request):

#         new_employee = Employee()

#         new_employee.city = request.data['city']
#         new_employee.phone = request.data['phone']

#         new