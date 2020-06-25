from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import ClientNote

class ClientNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ClientNote
        url = serializers.HyperlinkedIdentityField(
            view_name='clientnote',
            lookup_field='id'
        )
        fields = ('id', 'employee_id', 'client_id', 'comment', 'client')
        depth = 1

class ClientNotes(ViewSet):

    def create(self, request):

        new_client_note = ClientNote()

        new_client_note.employee_id = request.data['employee_id']
        new_client_note.client_id = request.data['client_id']
        new_client_note.comment = request.data['comment']

        new_client_note.save()

        serializer = ClientNoteSerializer(
            new_client_note, context={'request': request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            client_note = ClientNote.objects.get(pk=pk)
            serializer = ClientNoteSerializer(
                client_note, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        client_note = ClientNote.objects.get(pk=pk)
        
        client_note.comment = request.data['comment']

        client_note.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            client_note = ClientNote.objects.get(pk=pk)
            client_note.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ClientNote.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        try:
            cid = self.request.query_params.get('client_id')
            client_notes = ClientNote.objects.filter(id=cid)

            serializer = ClientNoteSerializer(
                client_notes, many=True, context={'request': request}
            )

            return Response(serializer.data)

        except ClientNote.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)