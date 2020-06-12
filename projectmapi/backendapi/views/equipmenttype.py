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
        fields = ('id', 'name')

class EquipmentTypes(ViewSet):

    def create(self, request):

        new_equipment_type = EquipmentType()
        new_equipment_type.name = request.data['name']

        new_equipment_type.save()

        serializer = EquipmentTypeSerializer(
            new_equipment_type, context={'request': request})

        return Response(serializer.data)

    def list(self, request):

        equipmenttypes = EquipmentType.objects.all()

        serializer = EquipmentTypeSerializer(
            equipmenttypes, many=True, context={'request': request}
        )

        return Response(serializer.data)
