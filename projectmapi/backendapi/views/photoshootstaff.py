from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import PhotoshootStaff

class PhotoshootStaffSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PhotoshootStaff
        url = serializers.HyperlinkedIdentityField(
            view_name='photoshootstaff',
            lookup_field='id'
        )
        fields = ('id', 'employee_id', 'photoshoot_id', 'photoshoot', 'employee')
        depth = 1

class PhotoshootStaffs(ViewSet):

    def create(self, request):

        new_staff = PhotoshootStaff()

        new_staff.employee_id = request.data['employee_id']
        new_staff.photoshoot_id = request.data['photoshoot_id']

        new_staff.save()

        serializer = PhotoshootStaffSerializer(
            new_staff, context={'request': request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            photoshootstaff = PhotoshootStaff.objects.get(pk=pk)
            serializer = PhotoshootStaffSerializer(
                photoshootstaff, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def update(self, request, pk=None):

        photoshootstaff = PhotoshootStaff.objects.get(pk=pk)

        photoshootstaff.employee_id = request.data['employee_id']
        photoshootstaff.photoshoot_id = request.data['photoshoot_id']

        photoshootstaff.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            photoshootstaff = PhotoshootStaff.objects.get(pk=pk)
            photoshootstaff.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except PhotoshootStaff.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        try:

            photoshootstaff = ""

            ps_id = self.request.query_params.get('photoshoot_id')
            emp_id = self.request.query_params.get('employee_id')

            if ps_id is not None:
                photoshootstaff = PhotoshootStaff.objects.filter(photoshoot_id=ps_id)

            if emp_id is not None:
                photoshootstaff = PhotoshootStaff.objects.filter(employee_id=emp_id)

            serializer = PhotoshootStaffSerializer(
                photoshootstaff, many=True, context={'request': request}
            )

            return Response(serializer.data)

        except PhotoshootStaff.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
