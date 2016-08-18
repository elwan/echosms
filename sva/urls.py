from django.conf.urls import patterns, url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns= [
    #url(r'^ajouter/',views.MessageCreate.as_view(),name="nouveau_message"),
    #url(r'^liste/',views.ListeMessage.as_view(),name="lister_message"),
    url(r'^msgenvoyer/',views.ListeMessageEnvoyes.as_view(),name="lister_message_envoyer"),
    #url(r'^editer/(?P<code>\w{6})$',views.MessageUpdate.as_view(),name="update_message"),
    #url(r'^delete/(?P<code>\w{6})$',views.MessageDelete.as_view(),name="delete_message"),
    #url(r'^envoi/(?P<code>\w{6})$',views.envoi_message,name="envoyer_message"),
    ##zone messages multiple
    url(r'^ajouter_multi/',views.MessageMultiCreate.as_view(),name="nouveau_message_multi"),
    url(r'editer_multi/(?P<code>\w{7})$',views.MessageMultiUpdate.as_view(),name="update_message_multi"),
    url(r'liste_multi/',views.ListeMultiMessage.as_view(),name="lister_message_multi"),
    url(r'^delete_multi/(?P<code>\w{7})$',views.MessageMultiDelete.as_view(),name="delete_message_multi"),
    url(r'^envoi_multi/(?P<code>\w{7})$',views.envoi_message_multi,name="envoyer_message_multi"),
    url(r'^dashbord/',views.tableau_de_bord,name="tableau_de_bord"),   
]


