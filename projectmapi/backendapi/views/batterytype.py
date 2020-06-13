from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import BatteryType

class BatteryTypeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = BatteryType
        url = serializers.HyperlinkedIdentityField(
            view_name='batterytype',
            lookup_field='id'
        )
        fields = ('id', 'name')

class BatteryTypes(ViewSet):

    def create(self, request):

        new_battery_type = BatteryType()
        new_battery_type.name = request.data['name']
        new_battery_type.save()

        serializer = BatteryTypeSerializer(
            new_battery_type, context={'request': request})

        return Response(serializer.data)


    def retrieve(self, request, pk=None):

        try:
            batterytype = BatteryType.objects.get(pk=pk)
            serializer = BatteryTypeSerializer(
                batterytype, context={'request': request}
            )
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    def update(self, request, pk=None):

        batterytype = BatteryType.objects.get(pk=pk)
        batterytype.name = request.data['name']
        batterytype.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk=None):

        try:
            batterytype = BatteryType.objects.get(pk=pk)
            batterytype.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):

        batterytypes = BatteryType.objects.all()

        serializer = BatteryTypeSerializer(
            batterytypes, many=True, context={'request': request}
        )

        return Response(serializer.data)