from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from contents.models import Contents_table


# Create your views here.

class ContentsSerializer(ModelSerializer):
    class Meta:
        model = Contents_table
        fields = ['title', 'detail']


class ContentsCreateAPI(APIView):
    def get(self, request):
        contents = Contents_table.objects.title

        return_data = ContentsSerializer(contents, many=True).data

        return Response(return_data)

    def post(self, request):
        contents = Contents_table.objects.create(
            title=request.data['title'],
            detail=request.data['detail'],
            pos_x=request.data['pos_x'],
            pos_y=request.data['pos_y'],
        )

        return_data = ContentsSerializer(contents).data

        return Response(return_data, status=201)


class ContentsDetailAPI(APIView):
    def get(self, request, member_id, crew_id):
        if member_id is not None:
            contents = Contents_table.objects.get(
                id=member_id
            )

            return_data = ContentsSerializer(contents).data

            return Response(return_data, status=200)

        elif crew_id is not None:
            contents = Contents_table.objects.get(
                id=crew_id
            )

            return_data = ContentsSerializer(contents).data

            return Response(return_data, status=200)

        else:
            return 404


    def put(self, request, member_id, crew_id):
        if member_id is not None:
            contents = Contents_table.objects.all()
            contents.put(
                title=request.data['title'],
                detail=request.data['detail'],
                pos_x=request.data['pos_x'],
                pos_y=request.data['pos_y'],
            )
            contents.save()
            return_data = ContentsSerializer(contents).data
            return Response(return_data, status=200)

        elif crew_id is not None:
            contents = Contents_table.objects.all()
            contents.put(
                title=request.data['title'],
                detail=request.data['detail'],
                pos_x=request.data['pos_x'],
                pos_y=request.data['pos_y'],
            )
            contents.save()
            return_data = ContentsSerializer(contents).data
            return Response(return_data, status=200)

        else:
            return 404


    def delete(self, request, member_id, crew_id):
        if member_id is not None:
            contents = Contents_table.objects.get(id=member_id)
            contents.delete()
            return Response(status=204)

        elif crew_id is not None:
            contents = Contents_table.objects.get(id=crew_id)
            contents.delete()
            return Response(status=204)

        else:
            return 404
