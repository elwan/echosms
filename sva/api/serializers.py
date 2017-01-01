from rest_framework.serializers import ModelSerializer
from sva.models import Message_Multi


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message_Multi
        fields = ['id', 'numero', 'sender', 'message', 'groupe_numeros', 'code']
