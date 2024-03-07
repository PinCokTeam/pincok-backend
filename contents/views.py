from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from contents.models import Contents
from contents.serializsers import Menu


# Create your views here.

class ContentsSerializer(ModelSerializer):
    class Meta:
        model = Contents
        fields = [Menu.contentfields]



class ContentsCreateAPI(APIView):
    def get(self, request):
        contents = Contents.objects.filter(Contents.title)

        return_data = ContentsSerializer(contents, many=True).data

        return Response(return_data)

    def post(self, request):
        serializer = ContentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contents = Contents.objects.create(
            title=serializer.validated_data['title'],
            detail=serializer.validated_data['detail'],
            pos_x=serializer.validated_data['pos_x'],
            pos_y=serializer.validated_data['pos_y'],
            member_id=serializer.validated_data['member_id'],
            crew_id=serializer.validated_data['crew_id'],
        )

        return_data = ContentsSerializer(contents).data

        return Response(return_data, status=201)


class ContentsDetailAPI(APIView):
    def get(self, request, member_id, crew_id):
        if member_id is not None:
            contents = Contents.objects.get(
                member_id=member_id
            )

            return_data = ContentsSerializer(contents).data

            return Response(return_data, status=200)

        elif crew_id is not None:
            contents = Contents.objects.get(
                crew_id=crew_id
            )

            return_data = ContentsSerializer(contents).data

            return Response(return_data, status=200)

        else:
            return 404


    def put(self, request, contents_id):
        if contents_id is not None:
            contents = Contents.objects.all()
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


    def delete(self, request, contents_id):
        if contents_id is not None:
            contents = Contents.objects.get(id=contents_id)
            contents.delete()
            return Response(status=204)

        else:
            return 404
