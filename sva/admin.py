from django.contrib import admin
from sva.models import Reponse, Message_Erreur, Message_Multi

# Register your models here.
# admin.site.register(Pays_Destination)
admin.site.register(Reponse)
admin.site.register(Message_Erreur)
admin.site.register(Message_Multi)
