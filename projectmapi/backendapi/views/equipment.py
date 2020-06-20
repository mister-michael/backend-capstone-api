from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import EquipmentModel


class EquipmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EquipmentModel
        url = serializers.HyperlinkedIdentityField(
            view_name='equipment',
            lookup_field='id'
        )
        fields = ('id', 'name', 'weight', 'battery_count',
                  'battery_type_id', 'wireless', 'return_date',
                  'equipment_type_id', 'rental_house_id', 'equipment_type', 'rental_house',)
        depth = 1


class Equipments(ViewSet):
    def create(self, request):

        new_equipment = EquipmentModel()

        new_equipment.name = request.data['name']
        new_equipment.weight = request.data['weight']
        new_equipment.battery_count = request.data['battery_count']
        new_equipment.battery_type_id = request.data['battery_type_id']
        new_equipment.wireless = request.data['wireless']
        new_equipment.return_date = request.data['return_date']
        new_equipment.equipment_type_id = request.data['equipment_type_id']
        new_equipment.rental_house_id = request.data['rental_house_id']

        new_equipment.save()

        serializer = EquipmentSerializer(
            new_equipment, context={'request': request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            equipment = EquipmentModel.objects.get(pk=pk)
            serializer = EquipmentSerializer(
                equipment, context={'request': request}
            )
            return Response(serializer.data)

        except Exception as ex:

            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        equipment = EquipmentModel.objects.get(pk=pk)

        equipment.name = request.data['name']
        equipment.weight = request.data['weight']
        equipment.battery_count = request.data['battery_count']
        equipment.battery_type_id = request.data['battery_type_id']
        equipment.wireless = request.data['wireless']
        equipment.return_date = request.data['return_date']
        equipment.equipment_type_id = request.data['equipment_type_id']
        equipment.rental_house_id = request.data['rental_house_id']

        equipment.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            equipment = EquipmentModel.objects.get(pk=pk)
            equipment.delete()

        except Equipment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        equipment = EquipmentModel.objects.all()

        serializer = EquipmentSerializer(
            equipment, many=True, context={'request': request}
        )

        return Response(serializer.data)
