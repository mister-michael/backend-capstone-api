from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import RentalHouse

class RentalHouseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RentalHouse
        url = serializers.HyperlinkedIdentityField(
            view_name='client',
            lookup_field='id'
        )
        fields = ('id', 'name', 'city', 
                'phone', 'email')

class RentalHouses(ViewSet):

    def create(self, request):

        new_rentalhouse = new_RentalHouse()

        new_rentalhouse.name = request.data['name']
        new_rentalhouse.city = request.data['city']
        new_rentalhouse.phone = request.data['phone']
        new_rentalhouse.email = request.data['email']

        new_rentalhouse.save()

        serializer = RentalHouseSerializer(
            new_rentalhouse, context={'request': request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            rentalhouse = RentalHouse.objects.get(pk=pk)
            serializer = RentalHouseSerializer(
                rentalhouse, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        rentalhouse = RentalHouse.objects.get(pk=pk)

        rentalhouse.name = request.data['name']
        rentalhouse.city = request.data['city']
        rentalhouse.phone = request.data['phone']
        rentalhouse.email = request.data['email']

        rentalhouse.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            rentalhouse = RentalHouse.objects.get(pk=pk)
            rentalhouse.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except RentalHouse.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        rentalhouses = RentalHouse.objects.all()

        serializer = RentalHouseSerializer(
            rentalhouses, many=True, context={'request': request}
        )

        return Response(serializer.data)