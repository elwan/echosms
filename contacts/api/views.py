from rest_framework.generics import ListAPIView, RetrieveAPIView
from contacts.models import Contact, Groupe
from .serializers import ContactSerializer, GroupeSerializer


class ContactListApiView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(contact_utilisateur=user)


class ContactDetailApiView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(contact_utilisateur=user)


class GroupeListApiView(ListAPIView):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer

    def get_queryset(self):
        user = self.request.user
        return Groupe.objects.filter(groupe_utilisateur=user)


class GroupeDetailApiView(RetrieveAPIView):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer

    def get_queryset(self):
        user = self.request.user
        return Groupe.objects.filter(groupe_utilisateur=user)
