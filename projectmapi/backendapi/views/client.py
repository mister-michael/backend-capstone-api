from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Client

class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        url = serializers.HyperlinkedIdentityField(
            view_name='client',
            lookup_field='id'
        )
        fields = ('id', 'first_name', 'last_name', 
                'phone', 'email', 'address', 'city', 
                'state', 'zip_code' )

class Clients(ViewSet):

    def create(self, request):

        new_client = Client()
        
        new_client.first_name = request.data['first_name']
        new_client.last_name = request.data['last_name']
        new_client.phone = request.data['phone']
        new_client.email = request.data['email']
        new_client.address = request.data['address']
        new_client.city = request.data['city']
        new_client.state = request.data['state']
        new_client.zip_code = request.data['zip_code']

        new_client.save()

        serializer = ClientSerializer(
            new_client, context={'request': request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
            serializer = ClientSerializer(
                client, context={'request': request})

            return Response(serializer.data)
        
        except Exception as ex:

            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        client = Client.objects.get(pk=pk)

        client.first_name = request.data['first_name']
        client.last_name = request.data['last_name']
        client.phone = request.data['phone']
        client.email = request.data['email']
        client.address = request.data['address']
        client.city = request.data['city']
        client.state = request.data['state']
        client.zip_code = request.data['zip_code']

        client.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
            client.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Client.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        clients = Client.objects.all()

        serializer = ClientSerializer(
            clients, many=True, context={'request': request}
        )

        return Response(serializer.data)