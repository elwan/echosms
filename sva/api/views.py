from rest_framework.generics import ListAPIView, RetrieveAPIView
from sva.models import Message_Multi
from .serializers import MessageSerializer


class MessageListApiView(ListAPIView):
    queryset = Message_Multi.objects.all()
    serializer_class = MessageSerializer


class MessageDetailApiView(RetrieveAPIView):
    queryset = Message_Multi.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'code'
