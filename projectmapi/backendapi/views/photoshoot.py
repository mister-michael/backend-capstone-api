from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Photoshoot

class PhotoshootSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Photoshoot
        url = serializers.HyperlinkedIdentityField(
            view_name='photoshoot',
            lookup_field='id'
        )
        fields = ('id', 'name', 'location', 'indoor', 
                    'date_scheduled', 'charge', 'paid', 'client')
        depth = 1

class Photoshoots(ViewSet):

    def create(self, request):

        new_photoshoot = Photoshoot()

        new_photoshoot.name = request.data['name']
        new_photoshoot.location = request.data['location']
        new_photoshoot.indoor = request.data['indoor']
        new_photoshoot.date_scheduled = request.data['date_scheduled']
        new_photoshoot.charge = request.data['charge']
        new_photoshoot.paid = request.data['paid']
        new_photoshoot.client_id = request.data['client_id']

        new_photoshoot.save()

        serializer = PhotoshootSerializer(
            new_photoshoot, context={'request': request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            photoshoot = Photoshoot.objects.get(pk=pk)
            serializer = PhotoshootSerializer(
                photoshoot, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    # def update(self, request, pk=None):
