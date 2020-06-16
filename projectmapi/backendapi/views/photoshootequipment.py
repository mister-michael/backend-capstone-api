from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import PhotoshootEquipment

class PhotoshootEquipmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PhotoshootEquipment
        url = serializers.HyperlinkedIdentityField(
            view_name='photoshootequipment',
            lookup_field='id'
        )
        fields = ('id', 'equipment_id', 'photoshoot_id', 'photoshoot', 'equipment')
        depth = 1
    
class PhotoshootEquipments(ViewSet):

    def create(self, request):

        new_pse = PhotoshootEquipment()

        new_pse.equipment_id = request.data['equipment_id']
        new_pse.photoshoot_id = request.data['photoshoot_id']

        new_pse.save()

        serializer = PhotoshootEquipmentSerializer(
            new_pse, context={'request': request}
        )

        return Response(serializer.data)