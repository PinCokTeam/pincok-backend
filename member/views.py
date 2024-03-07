from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from member.models import Member


# Create your views here.


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class MemberListAPI(APIView):
    def get(self, request):
        person = Member.objects.all()
        return Response(MemberSerializer(person, many=True).data)

    def post(self, request):
        # 튜플 형식 반환
        person, is_exist_person = Member.objects.get_or_create(
            name=request.data['name']
        )
        if is_exist_person:
            return Response(MemberSerializer(person).data, status=201)
        else:
            return Response(status=409)


class MemberDetailAPI(APIView):
    def get(self, request, id_):
        person = Member.objects.get(id=id_)
        return Response(MemberSerializer(person).data)

    def put(self, request, id_):
        person = Member.objects.get(id=id_)
        serializer = MemberSerializer(person, data=request.data)
        serializer.is_valid(raise_exception=True)  # 유효성 검사
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id_):
        person = Member.objects.get(id=id_)
        person.delete()
        return Response(status=204)
