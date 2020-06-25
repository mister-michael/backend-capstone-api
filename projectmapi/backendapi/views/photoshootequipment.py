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

    def retrieve(self, request, pk=None):
        try:
            pse = PhotoshootEquipment.objects.get(pk=pk)
            serializer = PhotoshootEquipmentSerializer(
                pse, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        
        pse = PhotoshootEquipment.objects.get(pk=pk)

        pse.equipment_id = request.data['equipment_id']
        pse.photoshoot_id = request.data['photoshoot_id']

        pse.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            pse = PhotoshootEquipment.objects.get(pk=pk)
            pse.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except PhotoshootEquipment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        pse = PhotoshootEquipment.objects.all()

        ps_id = self.request.query_params.get('photoshoot_id')

        eq_id = self.request.query_params.get('equipment_id')

        # inpack_psid = self.request.query_params.get('inpack')

        if ps_id is not None:
            pse = PhotoshootEquipment.objects.filter(photoshoot_id=ps_id)

        if eq_id is not None:
            pse = PhotoshootEquipment.objects.filter(equipment_id=eq_id)

        # if inpack_psid is not None:
        #     pse = PhotoshootEquipment.objects.exclude(photoshoot_id=inpack_psid).values_list('equipment_id', flat=True).distinct().all()

        serializer = PhotoshootEquipmentSerializer(
            pse, many=True, context={'request': request}
        )

        return Response(serializer.data)