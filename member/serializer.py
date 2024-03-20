from rest_framework.serializers import ModelSerializer

from member.models import Member


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name']


class MemberListSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ['name']
