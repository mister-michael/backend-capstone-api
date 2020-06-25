from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import PhotoshootNote

class PhotoshootNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PhotoshootNote
        url = serializers.HyperlinkedIdentityField(
            view_name='photoshootnote',
            lookup_field='id'
        )
        fields = ('id', 'employee_id', 'photoshoot_id', 'comment', 'photoshoot', 'employee')
        depth = 1

class PhotoshootNotes(ViewSet):

    def create(self, request):

        new_psn = PhotoshootNote()

        new_psn.employee_id = request.data['employee_id']
        new_psn.photoshoot_id = request.data['photoshoot_id']
        new_psn.comment = request.data['comment']

        new_psn.save()

        serializer = PhotoshootNoteSerializer(
            new_psn, context={'request': request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            psn = PhotoshootNote.objects.get(pk=pk)
            serializer = PhotoshootNoteSerializer(
                psn, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        psn = PhotoshootNote.objects.get(pk=pk)
        
        psn.comment = request.data['comment']

        psn.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            psn = PhotoshootNote.objects.get(pk=pk)
            psn.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except PhotoshootNote.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):

        try:
            ps_id = self.request.query_params.get('photoshoot_id')
            psn = PhotoshootNote.objects.filter(photoshoot_id=ps_id)

            serializer = PhotoshootNoteSerializer(
                psn, many=True, context={'request': request}
            )

            return Response(serializer.data)

        except PhotoshootNote.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

