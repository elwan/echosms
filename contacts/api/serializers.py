from rest_framework.serializers import ModelSerializer
from contacts.models import Contact, Groupe


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'nom', 'prenom', 'numero_telephone', 'photo', 'email_address']


class GroupeSerializer(ModelSerializer):

    class Meta:
        model = Groupe
        fields = ['id', 'nom_groupe', 'image_groupe', 'contacts', 'about']
