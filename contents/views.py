from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from contents.models import Contents
from contents.serializser import ContentsSerializer, ContentsListSerializer


# Create your views here.

class ContentsListCreateAPI(APIView):
    def get(self, request) -> Response:
        contents: QuerySet[Contents] = Contents.objects.all()
        return_data = ContentsListSerializer(contents, many=True).data

        return Response(return_data)

    def post(self, request):
        serializer = ContentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contents: Contents = Contents.objects.create(
            title=serializer.validated_data['title'],
            detail=serializer.validated_data['detail'],
            pos_x=serializer.validated_data['pos_x'],
            pos_y=serializer.validated_data['pos_y'],
            # member_id=serializer.validated_data['member_id'],
            # crew_id=serializer.validated_data['crew_id'],
        )

        # ContentImages.objects.create(content=contents)
        # ContentImages.objects.create(content_id=contents.id)

        return_data = ContentsSerializer(contents).data

        return Response(return_data, status=201)


class ContentsDetailAPI(APIView):
    def get(self, request, contents_id):
        contents: Contents = get_object_or_404(Contents, id=contents_id)
        return_data = ContentsSerializer(contents).data
        return Response(return_data, status=200)

    def put(self, request, contents_id):
        serializer = ContentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contents: Contents = get_object_or_404(Contents, id=contents_id)

        # contents: QuerySet[Contents] = Contents.objects.filter(id=contents_id)
        # if not contents.exists():
        #     return Response(status=404)
        # contents = contents.first()
        # if contents is None:
        #     return Response(status=404)

        # try:
        #     contents: Contents = Contents.objects.get(id=contents_id)
        # except Contents.DoesNotExist:
        #     return Response(status=404)

        contents.title = request.data["title"]
        contents.detail = request.data["detail"]
        contents.pos_x = request.data["pos_x"]
        contents.pos_y = request.data["pos_y"]
        contents.save()
        return_data = ContentsSerializer(contents).data
        return Response(return_data, status=200)

    def delete(self, request, contents_id):
        get_object_or_404(Contents, id=contents_id).delete()
        return Response(status=204)
