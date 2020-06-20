from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import EquipmentType

class EquipmentTypeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = EquipmentType
        url = serializers.HyperlinkedIdentityField(
            view_name='equipmenttype',
            lookup_field='id'
        )
        fields = ('id', 'name', 'equipment')

class EquipmentTypes(ViewSet):

    def create(self, request):

        new_equipment_type = EquipmentType()
        new_equipment_type.name = request.data['name']
        new_equipment_type.save()

        serializer = EquipmentTypeSerializer(
            new_equipment_type, context={'request': request})

        return Response(serializer.data)


    def retrieve(self, request, pk=None):

        try:
            equipmenttype = EquipmentType.objects.get(pk=pk)
            serializer = EquipmentTypeSerializer(
                equipmenttype, context={'request': request}
            )
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    def update(self, request, pk=None):

        equipmenttype = EquipmentType.objects.get(pk=pk)
        equipmenttype.name = request.data['name']
        equipmenttype.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk=None):

        try:
            equipmenttype = EquipmentType.objects.get(pk=pk)
            equipmenttype.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):

        equipmenttypes = EquipmentType.objects.all()

        serializer = EquipmentTypeSerializer(
            equipmenttypes, many=True, context={'request': request}
        )

        return Response(serializer.data)

    