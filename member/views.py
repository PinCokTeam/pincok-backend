from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from member.models import Member
from member.serializer import MemberListSerializer, MemberSerializer


# Create your views here.

class MemberCreateAPI(APIView):
    def get(self, request):
        member = Member.objects.all()
        return_data = MemberSerializer(member, many=True).data

        return Response(return_data)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        member = Member.objects.create(
            name=serializer.validated_data['name'],
        )

        return_data = MemberSerializer(member).data

        return Response(return_data, status=201)


class MemberDetailAPI(APIView):
    def get(self, request, member_id):
        member = get_object_or_404(Member, id=member_id)
        return_data = MemberSerializer(member).data
        return Response(return_data, status=200)

    def put(self, request, member_id):
        serializer = MemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        member = get_object_or_404(Member, id=member_id)
        member.name = request.data["name"]
        member.save()
        return_data = MemberSerializer(member).data
        return Response(return_data, status=200)

    def delete(self, request, member_id):
        get_object_or_404(Member, id=member_id).delete()
        return Response(status=204)

