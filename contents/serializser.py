from rest_framework.serializers import ModelSerializer

from contents.models import Contents


class ContentsSerializer(ModelSerializer):
    class Meta:
        model = Contents
        fields = ['title', 'detail', 'pos_x', 'pos_y']


class ContentsListSerializer(ModelSerializer):
    class Meta:
        model = Contents
        fields = ['title']