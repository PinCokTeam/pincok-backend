from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from crew.models import Crew


class CrewSerializer(ModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'


class CrewListAPI(APIView):
    def get(self, request) -> Response:
        crews = Crew.objects.all()
        return_data = CrewSerializer(instance=crews, many=True).data
        return Response(return_data)

    def post(self, request) -> Response:
        serializer = CrewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


class CrewDetailAPI(APIView):
    def get(self, request, crew_id: int) -> Response:
        crew = get_object_or_404(queryset=Crew, id=crew_id)
        serializer = CrewSerializer(instance=crew)
        return Response(data=serializer.data)

    def put(self, request, crew_id: int) -> Response:
        crew = get_object_or_404(queryset=Crew, id=crew_id)
        serializer = CrewSerializer(instance=crew, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def patch(self, request, crew_id: int) -> Response:
        crew = get_object_or_404(queryset=Crew, id=crew_id)
        serializer = CrewSerializer(instance=crew, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, crew_id: int) -> Response:
        crew = get_object_or_404(queryset=Crew, id=crew_id)
        crew.delete()
        return Response(status=204)
